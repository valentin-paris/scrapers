import requests
import json
import fileUtils
import DataUtils

'''
                                        GLOBAL VARIABLES
'''
querystring = {"noCache":"1565077788759-5428"}

headers = {
    'Accept': "application/json, text/plain, */*",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "fr",
    'Cache-Control': "private, max-age=0, no-cache",
    'channel': "b2c.public.hello.bank",
    'Connection': "keep-alive",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Postman-Token': "70c04ac6-111a-41d8-a87d-aa2dfe29fabc,b7fcf1d3-0a77-4459-9faa-c0db2d4504ea",
    'Host': "credit.hellobank.be",
    'Cookie': "TS017d8c48=0103eefa50b2377a9c2f21fabf9c547aa9d946a8a9c0124dcb44f2e1aa963f5f8ba0da6351674cc1603a884c98cf44f20f20e7c771; TS01114853=011bf91c22f66656111560ddcb680deb057903530477fbf1ba4da9b3ad01f5310d1dc401f48b0e1d096cd9152b8b84fae85477416b",
    'cache-control': "no-cache"
    }


loanCategories = {
    'Travaux': (763, 'HBNK0003'),
    'Voiture': (761, 'HBNK0001'),
    'Voiture occasion': (764, 'HBNK0002'),
    'Pret Personnel': (760, 'HBNK0004'),
    'Appareils Diditaux': (770, 'HBNK0005')
}

#this is for small loans like prêt pour appareils digitaux
smallLoanRange = list(range(500, 3000, 500))

#this range is made for big loans request
bigLoansRange = list(range(1250, 10000, 1250)) + list(range(10000, 37500, 2500))


'''
                                           FUNCTIONS
'''
#build the querry and make the request for a given price and category and returns the data as python object
def makeDataRequestFor(category, amount):
    url = "https://credit.hellobank.be/backend/simulation/loan/amount/{}/1/{}".format(amount, loanCategories[category][0])
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)

def addAttributeId(loanList, category):
    for loan in loanList:
        loan['productID'] = loanCategories[category][1]
        loan['type'] = category
    return loanList

def bankData(category):
    helloLoanData = []
    if category == 'Appareils Diditaux':
        for mnt in smallLoanRange:
            helloLoanData.append(addAttributeId(makeDataRequestFor(category, mnt), category))
    else:
        for mnt in bigLoansRange:
            helloLoanData.append(addAttributeId(makeDataRequestFor(category, mnt), category))
    return helloLoanData

#fetch the data for a category creates the groups and handle the file creation.
def helloLoanProcedure(category):
    tab_Column = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    dataMatrix = DataUtils.formatDataFrom(DataUtils.createGroups(bankData(category)), 'HELLO BANK')
    return DataUtils.processData(dataMatrix, tab_Column, 'HELLO BANK SCRAPING', category)

#this function is just for monitoring purposes in case of doubt it shows all the individual data and not in grouped forme
def showCompleteData(category):
    tab_Column = ['PROVIDER ', 'LOAN TYPE', 'AMOUNT', 'TERM', 'RATE']
    helloLoanData = []
    completeData = []
    if category == 'Appareils Diditaux':
        for mnt in smallLoanRange:
            helloLoanData.append(makeDataRequestFor(category, mnt))
    else:
        for mnt in bigLoansRange:
            helloLoanData.append(makeDataRequestFor(category, mnt))
    for loanList in helloLoanData:
        for loanElement in loanList:
            completeData.append(['HELLO BANK', category, loanElement['amount'], loanElement['duration'], loanElement['rate']])
    fileUtils.displayRates(tab_Column, completeData)

#                                           SCRAPER
#scrape all categories
def helloBankScraper():
    for category in loanCategories:
        return helloLoanProcedure(category)

helloBankScraper()


dataSample = [
   {
      'amount':'7750',
      'rate':'3.90',
      'duration':'12',
      'installment':'659.31',
      'grossAmount':'7911.72',
      'promo':None
   },
   {
      'amount':'7750',
      'rate':'3.90',
      'duration':'18',
      'installment':'443.73',
      'grossAmount':'7987.14',
      'promo':None
   },
   {
      'amount':'7750',
      'rate':'3.90',
      'duration':'24',
      'installment':'335.96',
      'grossAmount':'8063.04',
      'promo':None
   },
   {
      'amount':'7750',
      'rate':'3.90',
      'duration':'30',
      'installment':'271.31',
      'grossAmount':'8139.30',
      'promo':None
   },
   {
      'amount':'7750',
      'rate':'3.90',
      'duration':'36',
      'installment':'228.23',
      'grossAmount':'8216.28',
      'promo':None
   },
   {
      'amount':'7750',
      'rate':'3.90',
      'duration':'42',
      'installment':'197.46',
      'grossAmount':'8293.32',
      'promo':None
   },
   {
      'amount':'7750',
      'rate':'3.90',
      'duration':'48',
      'installment':'174.40',
      'grossAmount':'8371.20',
      'promo':None
   }
]




