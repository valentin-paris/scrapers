import requests
import json
import DataUtils


'''
    from here we will start adding a new product attribute to our object ie productID
    therefore we need to redefine data formating fonctions from the file dataUtils to 
    take those new changes into consideration  
'''

loanRangePerMonth = {
    24: list(range(501, 2500, 500)) + [2500],
    30: list(range(2501, 3700, 500)) + [3700],
    36: list(range(3701, 5600, 500)) + [5600],
    42: list(range(5601, 7500, 500)) + [7500],
    48: list(range(7501, 10000, 1000)) + [10000],
    60: list(range(10001, 15000, 1000)) + [15000],
    72: list(range(15001, 25000, 2500)) + [25000]
}

loantTypes = {
    'personal loan': ('30096', 'KBCX0001'),
    'new car': ('80301', 'KBCX0002'),
    '2nd hand car': ('80303', 'KBCX0003'),
    'renovation': ('60290', 'KBCX0004'),
    'energy loan': ('60293', 'KBCX0005')
}

def requestDataFor(lType, amount, term):
    url = "https://www.kbc.be/PSA/A058/service/calculateLoanSimulation/1"

    querystring = {"cb": "1566207137792"}

    headers = {
        'Connection': "keep-alive",
        'Content-Length': "181",
        'Sec-Fetch-Mode': "cors",
        'language': "fr",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        'Content-Type': "application/json;charset=UTF-8",
        'Accept': "application/json",
        'CSRF-Token': "undefined",
        'company': "0001",
        'Origin': "https://www.kbc.be",
        'Sec-Fetch-Site': "same-origin",
        'Cache-Control': "no-cache",
        'Postman-Token': "3c2e85fc-f7f6-4cf5-a4dc-6ed3e1cfa049,9e145398-33fa-4d0f-bd98-13c969d062aa",
        'Host': "www.kbc.be",
        'Accept-Encoding': "gzip, deflate",
        'cache-control': "no-cache"
    }

    payload = {
        "creditPurposeCode": {
            "T": "text",
            "V": loantTypes[lType][0]
        },
        "purchaseAmount": {
            "V": str(amount),
            "T": "decimal"
        },
        "loanAmount": {
            "V": str(amount),
            "T": "decimal"
        },
        "maturityMonthQuantity": {
            "V": str(term),
            "T": "decimal"
        }
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    return json.loads(response.text[6:])


def bankData():
    bankData = []
    print('KBC LOAN SCRAPE PROCESSING: ')
    for loanId in loantTypes:
        loanData = []
        for term in loanRangePerMonth:
            for amount in loanRangePerMonth[term]:
                for eachTerm in range(12, term + 6, 6):
                    print('.', end='')
                    loanJson = requestDataFor(loanId, amount, eachTerm)
                    loanJson['rate'] = float(loanJson['personalProperty']['yearInterestPercent']['V'])
                    loanJson['type'] = loanId
                    loanJson['amount'] = float(loanJson['personalProperty']['loanAmount']['V'])
                    loanJson['duration'] = eachTerm
                    loanJson['productID'] = loantTypes[loanId][1]
                    loanData.append(loanJson)
        print()
        bankData.append(loanData)
    return bankData


def createGroupsForKBC(bankData):
    loanGroups = {}
    for loanList in bankData:
        for loanElement in loanList:
            if (loanElement['type'], loanElement['productID'], loanElement['duration'], loanElement['rate']) not in \
                    loanGroups.keys():
                loanGroups[(loanElement['type'],loanElement['productID'], loanElement['duration'], loanElement['rate'])]\
                    = [loanElement['amount']]
            else:
                loanGroups[(loanElement['type'], loanElement['productID'], loanElement['duration'], loanElement['rate'])]\
                    .append(loanElement['amount'])
    return loanGroups


def formatDataFrom(groups, provider):
    frameToExport = []
    for eachGroup in groups:
        frameToExport.append([provider, eachGroup[0], eachGroup[1], min(map(int, groups[eachGroup])),
                              max(map(int, groups[eachGroup])), int(eachGroup[2]), float(eachGroup[3])])
    return frameToExport


def kBC_loan_scrape():
    tab_Column = ['PROVIDER ', 'LOAN TYPE', 'PRODUCT_ID', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    dataMatrix = formatDataFrom(createGroupsForKBC(bankData()), 'KBC')
    return DataUtils.processData(dataMatrix, tab_Column, 'KBC BANK SCRAPE', 'kbc_rates')



# kBC_loan_scrape()






dataSample = {
   "personalProperty": {
      "purchaseAmount": {
         "V": "15000",
         "E": "BUZcwhq2B6d5kEm/R9d/8Tw+gG4g/CjY0ylMtlHQOKI\u003d",
         "T": "decimal"
      },
      "loanAmount": {
         "V": "15000",
         "E": "C4cjCx4BBMHV74PfcOosKqrfeebuSKvTaYHWOPt3DGk\u003d",
         "T": "decimal"
      },
      "maturityMonthQuantity": {
         "V": "48",
         "E": "RCLtqvdPQ8M23QYzQRawO1MjUV05D81II2KRE+uAn/k\u003d",
         "T": "short"
      },
      "termAmount":{
         "V": "331.43",
         "E": "TFzH2Ptmn174iuuQ4QpyUPDcRtWXeXAo12eutcczW3o\u003d",
         "T": "decimal"
      },
      "yearCostPercent": {
         "V": "2.95000",
         "E": "9FUt/yXzcL5Qr6ikpSEkWsyEeTnKzZAd4qsyoZ8rMl4\u003d",
         "T": "decimal"
      },
      "yearInterestPercent": {
         "V": "2.95000",
         "E": "pQM0Dd8cZhASoX8yFy0d65vL3ys56Lx3s+oMy2lCPn0\u003d",
         "T": "decimal"
      },
      "totalLoanAmount": {
         "V": "15908.46",
         "E": "B7Cs2EZAQVMXmkjA603hTUpNIItfhr62NgyzLAGCoo8\u003d",
         "T": "decimal"
      }
   },
   "header": {
      "resultCode": {
         "V": "00",
         "T": "text"
      }
   }
}