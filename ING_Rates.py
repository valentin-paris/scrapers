import requests
import json
import DataUtils


headers = {
    'Connection': "keep-alive",
    'Content-Length': "24",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'X-Requested-With': "XMLHttpRequest",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    'Sec-Fetch-Mode': "cors",
    'Content-Type': "application/json; charset=UTF-8",
    'Cache-Control': "no-cache",
    'Postman-Token': "b9091c40-6854-4fac-927d-477e208877aa,919e76d9-230d-4b9c-af46-5b610ad18303",
    'Host': "promo.ing.be",
    'Accept-Encoding': "gzip, deflate",
    'cache-control': "no-cache"
    }


loanRange = list(range(1300, 25000, 2400)) + list(range(25000, 55000, 5000)) + list(range(55000, 135000, 10000))
wideRange = list(range(1300, 5000, 1000)) + list(range(5000, 15000, 2500)) + list(range(15000, 135000, 10000))


loansUrls = {
    'renovation': 'https://promo.ing.be/RenovationLoan/webservices/wsSimulation.asmx/GetSimulations',
    'mobility': 'https://promo.ing.be/Mobilityloan/webservices/wsSimulation.asmx/GetSimulations',
    'personal': 'https://promo.ing.be/ConvenienceLoan/webservices/wsSimulation.asmx/GetSimulations'
}

renovationLoanSubTypes = {
    "renovation": (1, 'INGX0002'),
    "energy": (2, 'INGX0003')
}

mobilityLoansSubTypes = {
        'new car': (1, 'INGX0004'),
        'new eco-car': (2, 'INGX0004'),
        'second-hand car (less than 3 years)': (3, 'INGX0005'),
        'second-hand car (3 years or more)': (4, 'INGX0005'),
        'electric bike': (5, 'INGX0004'),
        'new motorbike': (6, 'INGX0004'),
        'second-hand motorbyke (less than 3 years)': (7, 'INGX0005'),
        'second-hand motorbyke (3 years or more)': (8, 'INGX0005'),
        'new mobile home': (9, 'INGX0004'),
        'second-hand mobile home(less than 3 years)': (10, 'INGX0005'),
        'second-hand mobile home(3 years or more)': (11, 'INGX0005')
    }

personalLoanSubTypes = {
    'furniture': (1, 'INGX0001'),
    'household appliance': (2, 'INGX0001'),
    'computer and IT equipement': (3, 'INGX0001'),
    'other': (4, 'INGX0001')
}

def applyLoanRequest(amount, Ltype, url):
    rpayload = {"type": Ltype, "amount": amount}
    try:
        response = requests.request("POST", loansUrls[url], json=rpayload, headers=headers)
        return json.loads(response.text)
    except:
        print("VOTRE REQUETE N'A PAS PU ABOUTIR CE SITE EST MOMENTANEMENT INDISPONIBLE")


def getLoansData(loanType, subTypes):
    loanData = []
    for key in subTypes:
        loans = []
        lRange = wideRange if loanType == 'mobility' else loanRange
        for amt in lRange:
            print('.', end='')
            loans.append(applyLoanRequest(amt, subTypes[key][0], loanType))
        for loanObject in loans:
            for loan in loanObject['d']:
                loan['type'] = key
                loan['amount'] = loan['Amount']
                loan['duration'] = loan['Duration']
                loan['rate'] = loan['AnnualRate']
                loan['productID'] = subTypes[key][1]
                loanData.append(loan)
    print()
    return loanData


def bankData():
    print('ING LOAN SCRAPE PROCESSING: ')
    return [getLoansData('renovation', renovationLoanSubTypes), getLoansData('mobility', mobilityLoansSubTypes),
               getLoansData('personal', personalLoanSubTypes)]

def iNGLoanscraper():
    tab_Column = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    dataMatrix = DataUtils.formatDataFrom(DataUtils.createGroups(bankData()), 'ING')
    return DataUtils.processData(dataMatrix, tab_Column, 'ING SCRAPE', 'ing_rates')




# iNGLoanscraper()



