import json
import random
import DataUtils
import requests



def requestForData():
    params = (
        ('retailer', '2487635'),
        ('amount', '10000'),
        ('duration', '42'),
        ('materialCode', '502'),
        ('language', 'fr'),
        ('v-1559684081349', ''),
        ('v-1559684192192', ''),
    )

    data = {
        'v-browserDetails': '1',
        'theme': 'fimsim',
        'v-appId': 'fimsim-1274463091',
        'v-sh': '1080',
        'v-sw': '1920',
        'v-cw': '846',
        'v-ch': '911',
        'v-curdate': '1559684192192',
        'v-tzo': '-120',
        'v-dstd': '60',
        'v-rtzo': '-60',
        'v-dston': 'true',
        'v-vw': '846',
        'v-vh': '0',
        'v-loc': 'https://loan.carrefourfinance.be/fimsim/?retailer=2487635&amount=10000&duration=42&materialCode=502&&language=fr&fbclid=IwAR1gizN8cLzmboWhXLZG4e4JMxGbeBUMp_dLS5Ax6EjUpflUty4Xgg_959s&v-1559684081349',
        'v-wn': 'fimsim-1274463091-0.3835151505760399'
    }
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Content-type': "application/x-www-form-urlencoded",
        'Referer': "https://loan.carrefourfinance.be/fimsim/?retailer=2487635&amount=10000&duration=42&materialCode=502&&language=fr",
        'Sec-Fetch-Mode': "cors",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36Content-type:",
        'accept': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "7b658075-7cac-4492-aa5e-35dc9de15b5c,920db245-41ae-4a3b-ba7a-42b8fb99f938",
        'Host': "loan.carrefourfinance.be",
        'Cookie': "JSESSIONID=Wfs786CxqGWt3DH3D-SE_v_fJiierqZNFgQzu-sd.buywl0004:phenix-buywl0004; TS0181821e=016b073a458b3ead7e5da992cfc5508af95a98314a56e90d6105fe03edeb9d2e637b5f3b6042a24570afad135a2a3e812492425cc52a4db37ad282acfb3dbc6ed6901967e1; BIGipServer~ap-buyway_int_app_front_dmz-337~p-buyway-phenix-front-prod-80=rd337o00000000000000000000ffff0ad7b545o80; TS016b11db=016b073a4540c4048e58318c0c404fdec50140c83c6ba6b570223c5d8261167db5492ef2445c8e7e1bff8683afc2af8e018b63f459f3d1c47aa7891593d4f72e621c8f69e9",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "528",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.post('https://loan.carrefourfinance.be/fimsim/', params=params, data=data)
    return json.loads(json.loads(response.text)['uidl'])

#print(requestForData())

def bankData():
    dataList = requestForData()['state']['1']['materialCodesMapping'][1]
    list_of_Data = [dataList[random.randint(0, len(dataList)-1)]['rateRanges']]
    for loanList in list_of_Data:
        for loan in loanList:
            loan['duration'] = loan['minDuration']
            loan['amount'] = float(loan['minCreditAmount'])
            loan['rate'] = float(loan['taeg'])
            loan['type'] = 'All Loans'
            loan['productID'] = 'CAFI0001'
    return list_of_Data

# print(bankData())

def dataToExport(bankData, provider):
    frameToExport = []
    for loanList in bankData:
        for loan in loanList:
            frameToExport.append([provider, loan['productID'], loan['type'], loan['amount'], float(loan['maxCreditAmount']),
                                  loan['duration'], loan['maxDuration'], loan['rate']])
    return frameToExport

# print(dataToExport(bankData(), 'CAF'))

def carrefourLoanScraper():
    tab_Column = ['PROVIDER', 'PRODUCTID', 'PRODUCT TYPE', 'LOAN FROM', 'TO', 'MIN DURATION', 'MAX DURATION', 'RATE']
    dataMatrix = dataToExport(bankData(), 'CARREFOUR FINANCE')
    return DataUtils.process_crf_data(dataMatrix, tab_Column, 'CARREFOUR SCRAPE', 'carrefour_rates')

# carrefourLoanScraper()






