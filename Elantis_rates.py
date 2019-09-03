import requests
from bs4 import BeautifulSoup
import json
import ast
import DataUtils


def requestForData():
    url = "https://www.elantis.be/fr/simulateur-pret-a-temperament/"

    querystring = {"objective":"renovation","renovation-amount":"12.500"}

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "84fb7859-b2d0-40f9-bf3d-e05fd349b635,fd208e66-116f-4ba8-8590-61a2693ed30f",
        'Host': "www.elantis.be",
        'Cookie': "pll_language=fr",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    soup = BeautifulSoup(response.text, 'html.parser')

    return ast.literal_eval(json.loads(soup.find_all('script')[7].text[39:13300]))

def bankData():
    bank_data = []
    try:
        script_data = requestForData()
    except:
        script_data = {}
    for lType in script_data:
        data_for_type = []
        if lType == 'car':
            print(script_data[lType]['types'])
            for pdType in script_data[lType]['types']:
                if pdType['type'] == 'new':
                    for rates in pdType['rates']:
                        for rate in rates['rates']:
                            data_for_type.append({'type': 'NEW CAR LOAN',
                                                'productID': 'ELAN0004',
                                                'amount': rates['min'],
                                                'maxAmnt': rates['max'],
                                                'duration': rate['duration'],
                                                'rate': rate['taeg']

                                              })

                else:
                    for rates in pdType['rates']:
                        for rate in rates['rates']:
                            data_for_type.append({'type': '2dh_car LOAN',
                                                'productID': 'ELAN0005',
                                                'amount': rates['min'],
                                                'maxAmnt': rates['max'],
                                                'duration': rate['duration'],
                                                'rate': rate['taeg']

                                              })
            bank_data.append(data_for_type)
        elif lType == 'personal':
            data_for_type = []
            for pdType in script_data[lType]['types']:
                for rates in pdType['rates']:
                    for rate in rates['rates']:
                        data_for_type.append({'type': 'PERSONAL LOAN',
                                                'productID': 'ELAN0001',
                                                'amount': rates['min'],
                                                'maxAmnt': rates['max'],
                                                'duration': rate['duration'],
                                                'rate': rate['taeg']

                                              })
            bank_data.append(data_for_type)
        elif lType == 'renovation':
            for pdType in script_data[lType]['types']:
                if pdType['type'] == 'classic':
                    for rates in pdType['rates']:
                        for rate in rates['rates']:
                            data_for_type.append({'type': 'RENOVATION LOAN',
                                                  'productID': 'ELAN0004',
                                                  'amount': rates['min'],
                                                  'maxAmnt': rates['max'],
                                                  'duration': rate['duration'],
                                                  'rate': rate['taeg']

                                                  })

                else:
                    for rates in pdType['rates']:
                        for rate in rates['rates']:
                            data_for_type.append({'type': 'ENERGY LOAN',
                                                  'productID': 'ELAN0005',
                                                  'amount': rates['min'],
                                                  'maxAmnt': rates['max'],
                                                  'duration': rate['duration'],
                                                  'rate': rate['taeg']

                                                  })
            bank_data.append(data_for_type)
    return bank_data

def formatDataFromBank(bank_data, provider):
    frame_to_export = []
    for loanList in bank_data:
        for loan in loanList:
            frame_to_export.append([provider, loan['productID'], loan['type'], loan['amount'], loan['maxAmnt'],
                                    loan['duration'], loan['rate']])
    return frame_to_export

def elantisLoanScraper():
    print('ELANTIS SCRAPE PROCESSING ...')
    tab_col = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    return DataUtils.proc_data(bankData(), 'ELANTIS', 'ELANTIS SCRAPE', 'elantis_rates', tab_col)

elantisLoanScraper()







