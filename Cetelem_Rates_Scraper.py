import requests
import json
# import fileUtils
import DataUtils



loanCategories = {
                    'Prêt Voiture neuve': (761, 'CETE0002'),
                    'Prêt Voiture 2nd main lt 36 mois': (775, 'CETE0002'),
                    'Prêt Voiture 2nd main mt 36 mois': (764, 'CETE0003'),
                    'Prêt Personnel': (760, 'CETE0001'),
                    'Prêt Energie': (777, 'CETE0004'),
                    'Prêt Renovation': (763, 'CETE0005'),
                    'Prêt Etudes': (782, 'CETE0007')
                    }

smallLoansRange = list(range(1250, 5500, 750))

bigLoansRange = list(range(2500, 20000, 1500)) + list(range(20000, 45000, 5000)) + list(range(45000, 85000, 10000))


# request the website and return json data
def makeDataRequestFor(category, amount):
    querystring = {"noCache": "1565095706063-8754"}

    headers = {
        'Connection': "keep-alive",
        'Accept': "application/json, text/plain, */*",
        'Cache-Control': "private, max-age=0, no-cache",
        'Accept-Language': "fr",
        'channel': "b2c.public.cetelem",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        'Referer': "https://www.cetelem.be/fr/simulation-pret-personnel",
        'Accept-Encoding': "gzip, deflate, br",
        'Postman-Token': "b74ccaaa-ae00-48de-8398-59ca1ecd8704,5c92f791-64f3-4885-9d35-4e26a0ab17eb",
        'Host': "www.cetelem.be",
        'Cookie': "TS01ac33dc=0103eefa50bb1d367f2d78d8162a7d53364677060727f4038ec1a1550aa572d706b540a549d7229c3b7a363728e12d8a6430cd8bf7; TS01114853=011bf91c2272843799d21b02416ec157eaeff1113e09cad1f3d90039f31101cd0cc7c92c34ef5e6794b2f0e3356ee7760a79cf553e",
        'cache-control': "no-cache"
    }
    url = "https://www.cetelem.be/backend/simulation/loan/amount/{}/1/{}".format(amount, loanCategories[category][0])
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)


# add attributes to website json
def addAttributeID(loanList, category):
    for loan in loanList:
        loan['productID'] = loanCategories[category][1]
        loan["type"] = category
    return loanList

# perform the scraping
def cetelemLoanProcedure(category):
    tab_Column = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    loanData = []
    if category == 'Prêt Etudes':
        for mnt in smallLoansRange:
            print('.', end='')
            loanList = addAttributeID(makeDataRequestFor(category, mnt), category)
            loanData.append(loanList)
    elif category == 'Prêt Personnel':
        for mnt in list(range(1200, 2500, 500)) + bigLoansRange:
            print('.', end='')
            loanList = addAttributeID(makeDataRequestFor(category, mnt), category)
            loanData.append(loanList)
    else:
        for mnt in bigLoansRange:
            print('.', end='')
            loanList = addAttributeID(makeDataRequestFor(category, mnt), category)
            loanData.append(loanList)
    print()
    return DataUtils.data_processing_last(loanData, 'CETELEM', 'CETELEM SCRAPING', category, tab_Column)


def cetelemLoanScraper():
    print('CETELEM SCRAPE PROCESSING', end='')
    result = []
    for category in loanCategories:
        # print('PROCESSING', end='')
        result + cetelemLoanProcedure(category)
    return result


# cetelemLoanScraper()


#this shows how the data are stuctured from the web site
dataSample = [
   {
      'amount':'13500',
      'rate':'2.49',
      'duration':'12',
      'installment':'1140.05',
      'grossAmount':'13680.60',
      'promo':None
   },
   {
      'amount':'13500',
      'rate':'2.49',
      'duration':'18',
      'installment':'764.70',
      'grossAmount':'13764.60',
      'promo':None
   },
   {
      'amount':'13500',
      'rate':'2.49',
      'duration':'24',
      'installment':'577.03',
      'grossAmount':'13848.72',
      'promo':None
   },
   {
      'amount':'13500',
      'rate':'2.49',
      'duration':'30',
      'installment':'464.45',
      'grossAmount':'13933.50',
      'promo':None
   },
   {
      'amount':'13500',
      'rate':'2.49',
      'duration':'36',
      'installment':'389.40',
      'grossAmount':'14018.40',
      'promo':None
   },
   {
      'amount':'13500',
      'rate':'2.49',
      'duration':'42',
      'installment':'335.80',
      'grossAmount':'14103.60',
      'promo':None
   },
   {
      'amount':'13500',
      'rate':'2.49',
      'duration':'48',
      'installment':'295.61',
      'grossAmount':'14189.28',
      'promo':None
   },
   {
      'amount':'13500',
      'rate':'2.49',
      'duration':'54',
      'installment':'264.36',
      'grossAmount':'14275.44',
      'promo':None
   },
   {
      'amount':'13500',
      'rate':'2.49',
      'duration':'60',
      'installment':'239.36',
      'grossAmount':'14361.60',
      'promo':None
   }
]


# import DataUtils
# DataUtils.scrape_and_notify(cetelemLoanScraper(), "cetelem", DataUtils.test_mail)
