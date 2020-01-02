import requests
import json
import DataUtils

reqRangeAmnt = {
    30: list(range(2501, 3700, 500)),
    36: list(range(3701, 6000, 500)),
    42: [5601, 6500, 7500],
    48: [7501, 8500, 9500, 10000],
    60: list(range(10001, 17500, 2500)),
    84: list(range(15001, 100000, 15000))

}

loanPurposes = {'new_car': 'CREL0001',
                'second_hand_car': 'CREL0002',
                'renovation': 'CREL0003',
                'eco_energy': 'CREL0005'
                }

hLHeaders = {
    'authority': "www.crelan.be",
    'method': "POST",
    'path': "/credits-simulation-rs/loan-simulation/credit-rate-from-monthly-cost",
    'scheme': "https",
    'accept': "application/json, text/plain, */*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    'content-length': "175",
    'content-type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Cache-Control': "no-cache",
    'Postman-Token': "2248965b-9869-48c2-b44d-b3b8ecf17c02,1de28ed0-82d2-4caa-a830-e414bef5e5e4",
    'Host': "www.crelan.be",
    'Cookie': "visid_incap_1549027=cu5ueFVES1arcjasafZpWWm9Ul0AAAAAQUIPAAAAAABvsi/hSHTn9Iroi38523MD; incap_ses_770_1549027=WBnAG5FbOALXUqx1zZevCmm9Ul0AAAAAf+NhdpJMis49zoP8rVn9rw==; incap_ses_766_1549027=CpTmZb5dZ316bdnf2WGhCjjFU10AAAAAR35dUn6mAnU484Jfo//w+w==",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

hLMonthPaymentRange = list(range(100, 10000, 500)) + [10000]
hLDurationRange = list(range(10, 30, 2)) + [30]

def applyRequestFor(destination, amount, duration):
    url = "https://www.crelan.be/credits-simulation-rs/loan-simulation/credit-rate-from-amount"

    headers = {
        'authority': "www.crelan.be",
        'method': "POST",
        'path': "/credits-simulation-rs/loan-simulation/credit-rate-from-amount",
        'scheme': "https",
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        'content-length': "128",
        'content-type': "application/json; charset=UTF-8",
        'User-Agent': "PostmanRuntime/7.15.2",
        'Cache-Control': "no-cache",
        'Postman-Token': "a28eabec-af20-4702-95ad-bfa1f2995973,f4db9f6c-4faf-433e-b7d3-9754a8a3dd76",
        'Host': "www.crelan.be",
        'Cookie': "visid_incap_1549027=cu5ueFVES1arcjasafZpWWm9Ul0AAAAAQUIPAAAAAABvsi/hSHTn9Iroi38523MD; incap_ses_770_1549027=WBnAG5FbOALXUqx1zZevCmm9Ul0AAAAAf+NhdpJMis49zoP8rVn9rw==",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    payload = {
                "amount": amount,
                "destinationId": destination,
                "language": "NL",
                "periodType": "YEARLY",
                "periods": duration,
                "productTypeId": "CONSUMERLOAN"
    }
    try:
        response = requests.request("POST", url, json=payload, headers=headers)
        return json.loads(response.text)
    except:
        print("VOTRE REQUETE N'A PAS PU ABOUTIR CE SITE EST MOMENTANEMENT INDISPONIBLE")

# in the range rates there is a particularity with 2nd hand car loan so we develop a custum procedure for it
def bankData():
    bankData = []
    print('CRELAN SCRAPE PROCESSING: ')
    for purpose in loanPurposes:
        if purpose == 'second_hand_car':
            loanList = []
            for term in reqRangeAmnt:
                if term == 84:
                    for amt in reqRangeAmnt[term]:
                        for month in [13] + list(range(18, term - 18, 6)):
                            print('.', end='')
                            loan = applyRequestFor(purpose, amt, month)
                            for jsElement in loan['calculatedInterestTypes']:
                                if jsElement['rate']:
                                    loan['rate'] = jsElement['rate']['yearlyInterestRate']
                                    loan['duration'] = month
                                    loan['type'] = purpose
                                    loan['amount'] = amt
                                    loan['productID'] = loanPurposes[purpose]
                                    loanList.append(loan)
                else:
                    for amt in reqRangeAmnt[term]:
                        for month in [13] + list(range(18, term + 6, 6)):
                            print('.', end='')
                            loan = applyRequestFor(purpose, amt, month)
                            for jsElement in loan['calculatedInterestTypes']:
                                if jsElement['rate']:
                                    loan['rate'] = jsElement['rate']['yearlyInterestRate']
                                    loan['duration'] = month
                                    loan['type'] = purpose
                                    loan['amount'] = amt
                                    loan['productID'] = loanPurposes[purpose]
                                    loanList.append(loan)
            bankData.append(loanList)
        else:
            loanList = []
            for term in reqRangeAmnt:
                for amt in reqRangeAmnt[term]:
                    for month in [13] + list(range(18, term + 6, 6)):
                        print('.', end='')
                        loan = applyRequestFor(purpose, amt, month)
                        for jsElement in loan['calculatedInterestTypes']:
                            if jsElement['rate']:
                                loan['rate'] = jsElement['rate']['yearlyInterestRate']
                                loan['duration'] = month
                                loan['type'] = purpose
                                loan['amount'] = amt
                                loan['productID'] = loanPurposes[purpose]
                                loanList.append(loan)
            bankData.append(loanList)
        print()
    return bankData

def hLoanRequest(amount, period, category):
    homeLoanUrl = "https://www.crelan.be/credits-simulation-rs/loan-simulation/credit-rate-from-monthly-cost"
    payload = {
        "periodType": "YEARLY",
        "destinationId": "home",
        "productTypeId": "MORTGAGE",
        "amount": amount,
        "periods": period,
        "language": "NL",
        "selectedFormulae": category,
        "advantageRate": None
    }
    response = requests.request("POST", homeLoanUrl, json=payload, headers=hLHeaders)
    return json.loads(response.text)

def hl_bankdata():
    bankData = []
    hl_category = (
        ("", ["fixed"]),
        ("variable", ["1/1/1"]),
        ("variable", ["3/3/3"]),
        ("variable", ["5/5/5"]),
        ("variable", ["8/3/3"]),
        ("variable", ["10/5/5"]),
        ("variable", ["15/5/5"])
    )
    for category in hl_category:
        loan_data = []
        for amt in hLMonthPaymentRange:
            for period in hLDurationRange:
                print('.', end='')
                loanObject = hLoanRequest(amt, period, category[1])
                try:
                    loanObject['amount'] = amt
                    loanObject['duration'] = period
                    loanObject['type'] = loanObject['destinationId']
                    for i in range(len(loanObject['calculatedInterestTypes'])):
                        if i == 0:
                            loanObject['rate'] = loanObject['calculatedInterestTypes'][i]['rate']['yearlyInterestRate']
                            loanObject['category'] = loanObject['calculatedInterestTypes'][i]['interest_type_id']
                            loan_data.append(loanObject)
                        else:
                            loanObject2 = {}
                            loanObject2['rate'] = loanObject['calculatedInterestTypes'][i]['rate']['yearlyInterestRate']
                            loanObject2['category'] = loanObject['calculatedInterestTypes'][i]['interest_type_id']
                            loanObject2['amount'] = amt
                            loanObject2['duration'] = period
                            loanObject2['type'] = loanObject['destinationId']
                            loan_data.append(loanObject2)
                except:
                    pass
        bankData.append(loan_data)
        print()
    return bankData

# we had to redefine the functions due to the particularity of home loans data
def createGroupsForHomeLoan(bankData):
    loanGroups = {}
    for loanList in bankData:
        for loanElement in loanList:
            if (loanElement['type'], loanElement['duration'], loanElement['rate'],
                    loanElement['category']) not in loanGroups.keys():
                loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'],
                    loanElement['category'])] = [loanElement['amount']]
            else:
                loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'],
                     loanElement['category'])].append(loanElement['amount'])
    return loanGroups


def formatData_for_hloan(groups, provider):
    frameToExport = []
    for eachGroup in groups:
        frameToExport.append([provider,
                              eachGroup[0],
                              eachGroup[3],
                              min(map(int, groups[eachGroup])),
                              max(map(int, groups[eachGroup])),
                              int(eachGroup[1]),
                              eachGroup[2]])
    return frameToExport

def homeLoanScraper():
    print("CRELAN HOME LOAN SCRAPE PROCESSING ...")
    tab_Column = ['PROVIDER ', 'CATEGORY ', 'LOAN TYPE', ' PAY FROM \n(month payment in euros)', 'TO', ' FOR \n (duration in years)',
                  'RATE \n (base rate)']
    dataMatrix = formatData_for_hloan(createGroupsForHomeLoan(hl_bankdata()),'CRELAN')
    # fileUtils.displayRates(tab_Column, dataMatrix)
    return DataUtils.processData(dataMatrix, tab_Column, 'CRELAN SCRAPE', 'crelan_homeLoans')

def crelanLoansScraper():
    tab_Column = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    return DataUtils.data_processing_last(bankData(), "CRELAN", "CRELAN SCRAPE", "crelan_rates", tab_Column)


# DataUtils.scrape_and_notify(crelanLoansScraper(), "crelan", DataUtils.test_mail)


# homeLoanScraper()














