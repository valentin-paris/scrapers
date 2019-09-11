import requests
from bs4 import BeautifulSoup
import re
import ast
import DataUtils


producTypes = {
    'RENOVATION LOAN' : {
        'url':'https://www.cofidis.be/fr/pret-travaux.php',
        'productID': 'COFI0003'
    },
    'PERSONAL LOAN': {
        'url': 'https://www.cofidis.be/fr/pret-personnel.php',
        'productID': 'COFI0001'
    },
    '2ND_HAND_CAR LOAN': {
        'url': 'https://www.cofidis.be/fr/pret-voiture-occasion.php',
        'productID': 'COFI0002'
    },

}


def requestDataforUrl(product):
    url = producTypes[product]['url']
    headers = {
        'User-Agent': "PostmanRuntime/7.16.3",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "fcd88eea-63ae-416b-9d9b-ba148ef78fe9,2d67f32e-69ff-433e-b6b9-426d6fd94700",
        'Host': "www.cofidis.be",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "nid=E0283035FA0FFA7582F10A9AFF6B2C5B62B7B1A0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_scripts = soup.find_all('script')
    for script in all_scripts:
        if 'allsimuJsonA' in script.text:
            try:
                return ast.literal_eval(re.search('{.*}', script.text).group(0))
            except:
                return {}

def computeRate(rateString):
    try:
        rate_num = rateString.replace(',', '.')
        return float(rate_num[:5])
    except:
        rate_num = rateString.replace(',', '.')
        return float(rate_num[:4])

def data_for_product(product):
    data = []
    loanData = requestDataforUrl(product)
    for loanAmnt in loanData['simu']['mnt']:
        for loanJson in loanAmnt['am']['am']:
            data.append(dict(type=product, amount=loanAmnt['m'], rate=computeRate(loanJson['a']), duration=loanJson['d'],
                             productID=producTypes[product]['productID']))
    return data

def bankData():
    bank_data = []
    for pdt in producTypes:
        bank_data.append(data_for_product(pdt))
    return bank_data

def cofidisLoanScraper():
    print('COFIDIS SCRAPE PROCESSING ...')
    tab_col = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    return DataUtils.proc_data(bankData(), 'COFIDIS', 'COFIDIS SCRAPE', 'cofidis_rate', tab_col)




# cofidisLoanScraper()


