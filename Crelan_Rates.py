import requests
import json
import DataUtils

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


reqRangeAmnt = {
    30: list(range(2501, 3700, 500)),
    36: list(range(3701, 6000, 500)),
    42: [5601, 6500, 7500],
    48: [7501, 8500, 9500, 10000],
    60: list(range(10001, 17500, 2500)),
    84: list(range(15001, 100000, 15000))

}

loanPurposes = ('new_car', 'second_hand_car', 'renovation', 'eco_energy')

homeLoanUrl = "https://www.crelan.be/credits-simulation-rs/loan-simulation/credit-rate-from-monthly-cost"

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

#in the range rates there is a particularity with 2nd hand car loan so we develop a custum procedure for it
def bankData():
    bankData = []
    for purpose in loanPurposes:
        if purpose == 'second_hand_car':
            loanList = []
            for term in reqRangeAmnt:
                if term == 84:
                    for amt in reqRangeAmnt[term]:
                        for month in [13] + list(range(18, term - 18, 6)):
                            loan = applyRequestFor(purpose, amt, month)
                            for jsElement in loan['calculatedInterestTypes']:
                                if jsElement['rate']:
                                    loan['rate'] = jsElement['rate']['yearlyInterestRate']
                                    loan['duration'] = month
                                    loan['type'] = purpose
                                    loan['amount'] = amt
                                    loanList.append(loan)
                else:
                    for amt in reqRangeAmnt[term]:
                        for month in [13] + list(range(18, term + 6, 6)):
                            loan = applyRequestFor(purpose, amt, month)
                            for jsElement in loan['calculatedInterestTypes']:
                                if jsElement['rate']:
                                    loan['rate'] = jsElement['rate']['yearlyInterestRate']
                                    loan['duration'] = month
                                    loan['type'] = purpose
                                    loan['amount'] = amt
                                    loanList.append(loan)
            bankData.append(loanList)
        else:
            loanList = []
            for term in reqRangeAmnt:
                for amt in reqRangeAmnt[term]:
                    for month in [13] + list(range(18, term + 6, 6)):
                        loan = applyRequestFor(purpose, amt, month)
                        for jsElement in loan['calculatedInterestTypes']:
                            if jsElement['rate']:
                                loan['rate'] = jsElement['rate']['yearlyInterestRate']
                                loan['duration'] = month
                                loan['type'] = purpose
                                loan['amount'] = amt
                                loanList.append(loan)
            bankData.append(loanList)
    return bankData


def hLoanRequest(amount, period):
    payload = {
        "periodType": "YEARLY",
        "destinationId": "home",
        "productTypeId": "MORTGAGE",
        "amount": amount,
        "periods": period,
        "language": "NL",
        "selectedFormulae": ["1/1/1", "3/3/3"],
        "advantageRate": None
    }
    response = requests.request("POST", homeLoanUrl, json=payload, headers=hLHeaders)
    return json.loads(response.text)

def hLoanData():
    bankData = []
    for amt in hLMonthPaymentRange:
        loanData = []
        for period in hLDurationRange:
            loanObject = hLoanRequest(amt, period)
            loanObject['amount'] = amt
            loanObject['duration'] = period
            loanObject['type'] = loanObject['destinationId']
            loanObject['rate_2'] = '-'
            for i in range(len(loanObject['calculatedInterestTypes'])):
                if i == 0 and loanObject['calculatedInterestTypes'][i]['rate']:
                    loanObject['rate'] = loanObject['calculatedInterestTypes'][i]['rate']['yearlyInterestRate']
                elif loanObject['calculatedInterestTypes'][i]['rate']:
                    loanObject['rate_{}'.format(i)] = loanObject['calculatedInterestTypes'][i]['rate']['yearlyInterestRate']
            loanData.append(loanObject)
        bankData.append(loanData)
    return bankData

#we had to redefine the functions due to the particularity of home loans data
def createGroupsForHomeLoan(bankData):
    loanGroups = {}
    for loanList in bankData:
        for loanElement in loanList:
            if (loanElement['type'], loanElement['duration'], loanElement['rate'], loanElement['rate_1'],
                    loanElement['rate_2']) not in loanGroups.keys():
                loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'], loanElement['rate_1'],
                    loanElement['rate_2'])] = [loanElement['amount']]
            else:
                loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'], loanElement['rate_1'],
                    loanElement['rate_2'])].append(loanElement['amount'])
    return loanGroups

def formatDataFrom(groups, provider):
    frameToExport = []
    for eachGroup in groups:
        frameToExport.append([provider, eachGroup[0], min(map(int, groups[eachGroup])), max(map(int, groups[eachGroup]))
                                 , int(eachGroup[1]), float(eachGroup[2]), float(eachGroup[3]), str(eachGroup[4])])
    return frameToExport

def homeLoanScraper():
    tab_Column = ['PROVIDER ', 'LOAN TYPE', 'PAY FROM \n (month payment in euros)', 'TO', 'FOR \n (duration in years)',
                  'RATE \n (starting rate)', 'REVISED \n(rates can be revised on a 3 years period)', 'REVISED_2']
    dataMatrix = formatDataFrom(createGroupsForHomeLoan(hLoanData()),'CRELAN')
    DataUtils.processData(dataMatrix, tab_Column, 'CRELAN SCRAPE', 'crelan_homeLoans')

def crelanLoansScraper():
    tab_Column = ['PROVIDER ', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    dataMatrix = DataUtils.formatDataFrom(DataUtils.createGroups(bankData()), 'CRELAN')
    DataUtils.processData(dataMatrix, tab_Column, 'CRELAN SCRAPE', 'crelan_rates')
    homeLoanScraper()

crelanLoansScraper()





#for testing purposes
sampledata = {
   "destinationId":"home",
   "productTypeId":"MORTGAGE",
   "calculatedInterestTypes":[
      {
         "rate":{
            "rateType":"BASIC",
            "monthlyPayment":5000.00,
            "monthlyPaymentBestCase":4337.68,
            "monthlyPaymentWorstCase":5475.66,
            "yearlyInterestRate":2.93,
            "yearlyCostRate":3.01,
            "loanAmount":520521.59,
            "loanAmountBestCase":600000.00,
            "loanAmountWorstCase":475304.82,
            "totalCosts":602083.00,
            "totalCostsBestCase":522604.60,
            "totalCostsWorstCase":659162.20
         },
         "interest_type_id":"1/1/1 +3/-3"
      },
      {
         "rate":{
            "rateType":"BASIC",
            "monthlyPayment":5000.00,
            "monthlyPaymentBestCase":4541.13,
            "monthlyPaymentWorstCase":5478.26,
            "yearlyInterestRate":2.74,
            "yearlyCostRate":2.82,
            "loanAmount":525157.30,
            "loanAmountBestCase":578223.44,
            "loanAmountWorstCase":479310.42,
            "totalCosts":602083.00,
            "totalCostsBestCase":547018.60,
            "totalCostsWorstCase":659474.20
         },
         "interest_type_id":"3/3/3 +2/-2"
      },
      {
         "rate":{
            "rateType":"BASIC",
            "monthlyPayment":5000.00,
            "monthlyPaymentBestCase":4376.31,
            "monthlyPaymentWorstCase":5659.66,
            "yearlyInterestRate":2.74,
            "yearlyCostRate":2.82,
            "loanAmount":525157.30,
            "loanAmountBestCase":600000.00,
            "loanAmountWorstCase":463947.95,
            "totalCosts":602083.00,
            "totalCostsBestCase":527240.20,
            "totalCostsWorstCase":681242.20
         },
         "interest_type_id":"3/3/3 +5/-5"
      }
   ]
}








