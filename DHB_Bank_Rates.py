import requests
import json
import DataUtils
import urllib3


loanAmtRange = list(range(5000, 14000, 500)) + list(range(14000, 101000, 1000))

dHBLoanTypes = {
    "personal": (1, 'DHBX0001')
}


def makeRequestFor(creditType, amount, duration):
    url = "https://loans.dhbbank.com/BelgiumLoanAppForm/Home/CalculateInterestRate"
    headers = {
        'Connection': "keep-alive",
        'Content-Length': "52",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Origin': "https://loans.dhbbank.be",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36",
        'Sec-Fetch-Mode': "cors",
        'Content-Type': "application/json;",
        'Sec-Fetch-Site': "same-origin",
        'Cache-Control': "no-cache",
        'Postman-Token': "b41e2ead-3420-4d32-94e9-72900c6d1caf,12d5e852-61e2-4a75-8e13-80a99fd0cbec",
        'Host': "loans.dhbbank.be",
        'Accept-Encoding': "gzip, deflate",
        'cache-control': "no-cache"
    }
    try:
        payload2 = {
            "CreditId": creditType,
            "Month": duration,
            "InterestAmount": amount
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.request("POST", url, json=payload2, headers=headers, verify=False)
        return json.loads(response.text)
    except:
        print('THIS WEBSITE IS NOT AVAILABLE AT THE MOMENT')
        return None


def bankData():
    bankData = []
    for lType in dHBLoanTypes:
        loanData = []
        for amnt in loanAmtRange:
            print('.', end='')
            loanJson = makeRequestFor(dHBLoanTypes[lType][0], amnt, duration=36)
            try:
                loanJson['rate'] = loanJson['InterestModel']['InterestRate']
                loanJson['amount'] = amnt
                loanJson['duration'] = 36
                loanJson['type'] = lType
                loanJson['productID'] = dHBLoanTypes[lType][1]
                loanData.append(loanJson)
            except:
                loanJson = {}
                print('OUPS this is not a valid request!')
            if loanJson:
                for term in range(42, loanJson['MonthlyModel']['MonthMax'] + 12, 12):
                    moreLoan = makeRequestFor(dHBLoanTypes[lType][0], amnt, term)
                    try:
                        moreLoan['rate'] = moreLoan['InterestModel']['InterestRate']
                        moreLoan['amount'] = amnt
                        moreLoan['duration'] = term
                        moreLoan['type'] = lType
                        moreLoan['productID'] = dHBLoanTypes[lType][1]
                        loanData.append(moreLoan)
                    except:
                        print()
                        print("OUPS this is not a valid request!")
        print()
        bankData.append(loanData)

    return bankData


def dHBLoanScraper():
    print("DHB LOAN SCRAPER PROCESSING:")
    tab_Column = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    return DataUtils.data_processing_last(bankData(), 'DHB BANK', 'DHB SCRAPE', 'dhb_rates', tab_Column)




