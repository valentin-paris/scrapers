import requests
import json
import DataUtils
import time

url = "https://loans.dhbbank.com/BelgiumLoanAppForm/Home/CalculateInterestRate"

headers = {
    'Connection': "keep-alive",
    'Content-Length': "53",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'X-Requested-With': "XMLHttpRequest",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    'Sec-Fetch-Mode': "cors",
    'Content-Type': "application/json;",
    'Origin': "https://loans.dhbbank.com",
    'Sec-Fetch-Site': "same-origin",
    'Referer': "https://loans.dhbbank.com/BelgiumLoanAppForm?langue=fr",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    'Cache-Control': "no-cache",
    'Postman-Token': "bfff3f0a-e283-44f8-8e31-a9a9e2db5005,d480cc24-d0b0-417b-87e6-9d31a2f2820e",
    'Host': "loans.dhbbank.com",
    'cache-control': "no-cache"
    }

loanAmtRange = list(range(5000, 20500, 500)) + list(range(21000, 101000, 1000))

dHBLoanTypes = {
    "personal": (1, 'DHBX0001')
}


def makeRequestFor(creditType, amount, duration):
    payload2 = {
                "CreditId": creditType,
                "Month": duration,
                "InterestAmount": amount
    }
    response = requests.request("POST", url, json=payload2, headers=headers, verify=False)
    return json.loads(response.text)


def bankData():
    bankData = []
    for lType in dHBLoanTypes:
        loanData = []
        for amnt in loanAmtRange:
            loanJson = makeRequestFor(dHBLoanTypes[lType][0], amnt, duration=24)
            loanJson['rate'] = loanJson['InterestModel']['InterestRate']
            loanJson['amount'] = amnt
            loanJson['duration'] = 24
            loanJson['type'] = lType
            loanJson['productID'] = dHBLoanTypes[lType][1]
            loanData.append(loanJson)
            for term in range(36, loanJson['MonthlyModel']['MonthMax']+12, 12):
                moreLoan = makeRequestFor(dHBLoanTypes[lType][0], amnt, term)
                print('amount: ', amnt)
                print()
                print('term ', term)
                print()
                print(moreLoan)
                print()
                # if not moreLoan['InterestModel']['InterestRate']:
                moreLoan['rate'] = moreLoan['InterestModel']['InterestRate']
                moreLoan['amount'] = amnt
                moreLoan['duration'] = term
                moreLoan['type'] = lType
                moreLoan['productID'] = dHBLoanTypes[lType][1]
                print('OK')
                loanData.append(moreLoan)
        bankData.append(loanData)
    return bankData


# def createGroupsForDHB(bankData):
#     loanGroups = {}
#     for loanList in bankData:
#         for loanElement in loanList:
#             if (loanElement['type'], loanElement['duration'],
#                             loanElement['rate']) not in loanGroups.keys():
#                 loanGroups[(loanElement['type'], loanElement['duration'],
#                             loanElement['rate'])] = [loanElement['amount']]
#             else:
#                 loanGroups[(loanElement['type'], loanElement['duration'],
#                             loanElement['rate'])].append(loanElement['amount'])
#     return loanGroups



def formatDataFrom(groups, provider):
    frameToExport = []
    for eachGroup in groups:
        frameToExport.append([provider, eachGroup[3], eachGroup[0], min(map(int, groups[eachGroup])), max(map(int, groups[eachGroup]))
                                 ,int(eachGroup[1]), float(eachGroup[2])])
    return frameToExport


# def formatDataFrom2(groups, provider):
#     frameToExport = []
#     for eachGroup in groups:
#         frameToExport.append([provider, eachGroup[3], eachGroup[0], min(map(int, groups[eachGroup])),
#                               max(map(int, groups[eachGroup])), int(eachGroup[1]), float(eachGroup[2])])
#     return frameToExport



def dHBLoanScraper():
    tab_Column = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    dataMatrix = DataUtils.formatDataFrom(DataUtils.createGroups(bankData()), 'DHB_BANK')
    return DataUtils.processData(dataMatrix, tab_Column, 'DHB SCRAPE', 'dhb_rates')



dHBLoanScraper()

dataSample = {
   "CreditModel": None,
   "MonthlyModel": {
      "MonthMax": 120,
      "MonthMin": 24
   },
   "InterestModel": {
      "InterestRate": 6.50,
      "CreditType": 1,
      "Calculation": 1120.41
   }
}




