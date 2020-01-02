import requests
import json
import time
import DataUtils
import math




cphProducts = {
                'personal': (30, 'CPHX0001'),
                'new car': (110, 'CPHX0004'),
                'second hand car under 24 months': (116, 'CPHX0004'),
                'second hand car under 60 months': (117, 'CPHX0005'),
                'renovation max 84 months': (12, 'CPHX0002'),
                'renovation 84-120 months': (56, 'CPHX0002'),
                'energy chauffage': (71, 'CPHX0003'),
                'energy photovoltaique': (74, 'CPHX0003'),
                'energy chassis double vitrage': (76, 'CPHX0003'),
                'energy isolation toiture': (77, 'CPHX0003'),
                'energy autres': (70, 'CPHX0003')
              }


loanRateAmt = list(range(1250, 10000, 1250)) + list(range(10000, 50000, 5000)) + list(range(50000, 110000, 10000))

def applyLoanRequest(amount, product):
    url = "https://mycph.cph.be/api/Simulation"
    headers = {
        'Connection': "keep-alive",
        'Content-Length': "94",
        'Sec-Fetch-Mode': "cors",
        'X-XSRF-Token': "1o1MGWzKeFsxHhUwTmHWa8YGs0G3NXbBZnM5JhnD4GwvKaKK3qr1Glvtxu8mkALVI1XI8EjDTiGvc8byTsE_1tkpJKo1",
        'Accept-Language': "fr-BE",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        'Content-Type': "application/json",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'X-Requested-With': "XMLHttpRequest",
        'Origin': "https://mycph.cph.be",
        'Sec-Fetch-Site': "same-origin",
        'Cache-Control': "no-cache",
        'Postman-Token': "02e02a41-f729-4544-81b4-c6f2b8f8ab32,9e6d355f-4a51-4e99-9f2d-2a35b8acd36a",
        'Host': "mycph.cph.be",
        'Cookie': "ApplicationGatewayAffinity=26c356c7bd253fe0307342d6fd2bf03d72cb588088d2a8e07c409d599f21e87e",
        'Accept-Encoding': "gzip, deflate",
        'cache-control': "no-cache"
    }

    payload = {
                "amount": amount,
                "productID": cphProducts[product][0],
                "monthly": amount,
                "method": "M",
                "inputDuration": 0,
                "deposit": False
    }
    try:
        response = requests.request("POST", url, json=payload, headers=headers)
        return json.loads(response.text)
    except:
        print("VOTRE REQUETE N'A PAS PU ABOUTIR CE SITE EST MOMENTANEMENT INDISPONIBLE")

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

#here we set a sleep time of 2 seconds between request bcoz the api only allows a limited amount of 1 request each second
def bankData():
    loanData = []
    print('CPH SCRAPE PROCESSING ')
    for pdt in cphProducts:
        amtData = []
        for amt in loanRateAmt:
            print('.', end='')
            time.sleep(2)
            loanJsonList = applyLoanRequest(amt, pdt)
            for loanObject in loanJsonList:
                loanObject['type'] = pdt
                loanObject['rate'] = truncate(loanObject['rate'] * 100, 2)
                loanObject['productID'] = cphProducts[pdt][1]
                amtData.append(loanObject)
        loanData.append(amtData)
        print()
    return loanData

def cphLoansScraper():
    tab_Column = ['PROVIDER ', 'PRODUCT_ID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    # return DataUtils.proc_data(bankData(), 'CPH', 'CPH SCRAPE', 'cph_rates', tab_Column)
    return DataUtils.data_processing_last(bankData(), 'CPH', 'CPH SCRAPE', 'cph_rates', tab_Column)


# cphLoansScraper()

# DataUtils.scrape_and_notify(cphLoansScraper(), "CPH", DataUtils.test_mail)

