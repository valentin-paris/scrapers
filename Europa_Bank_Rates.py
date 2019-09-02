import requests
import json
import fileUtils
import DataUtils

loanTypes = {
    'PERSONAL LOAN': ('PL', 'EURO0001'),
    'NEW CAR LOAN': ('NW', 'EURO0002'),
    '2ND HAND CAR LOAN': ('TW', 'EURO003'),
    'OTHERS VEHICULES LOAN': ('AD', 'EURO004'),
    'RENOVATION LOAN': ('RL', 'EURO0004')
}

loanRange = list(range(2500, 10000, 1000)) + list(range(10000, 30000, 2500)) + list(range(30000, 110000, 10000))

def makeRequestFor(lType, amount):
    url = "https://www.europabank.be/WebsiteAPI/rest/loan/amounts"

    querystring = {"type": loanTypes[lType][0], "bedrag": amount}

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "7839d327-280c-49bc-93f7-9a6bf8ea7fe5,66842b60-1f17-4db1-9270-0325557704bc",
        'Host': "www.europabank.be",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)

def addAttributes(loan, lType, amount, duration, rate):
        loan['type'] = lType
        loan['amount'] = amount
        loan['productID'] = loanTypes[lType][1]
        loan['rate'] = rate
        loan['duration'] = duration

def bankData():
    bankdata = []
    for ltype in loanTypes:
        data_for_type = []
        for amt in loanRange:
            try:
               print('.', end='')
               loanList = makeRequestFor(ltype, amt)[0]['looptijd']
               for loan in loanList:
                 addAttributes(loan, ltype, amt, loan['maanden'], loan['jkp'])
                 data_for_type.append(loan)
            except:
             print('THE LINK {} FOR EUROPA BANK IS NOT AVAILABLE FOR THE MOMENT'.format(ltype))
             break
        bankdata.append(data_for_type) if data_for_type else bankdata + data_for_type
    return bankdata



def processData(dataMatrix, tab_Column, directoryName, fileName):
    fileUtils.displayRates(tab_Column, dataMatrix)
    return fileUtils.upToDate(fileName, directoryName, dataMatrix, tab_Column, [])

def europaLoanScraper():
   print('EUROPA BANK LOAN SCRAPE PROCESSING: ')
   tab_col = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
   return DataUtils.proc_data(bankData(), 'EUROPA BANK', 'EURO_BANK SCRAPE', 'euro_bank_rates', tab_col)









