import requests
import json
import DataUtils


loanTypes = {
    'PERSONAL LOAN': ('539efc82-8caa-4edd-93d1-8168d3f310fe', 'BPOS0005'),
    'NEW CAR': ('afc2a560-93ad-46d4-8745-308cad87c9b7', 'BPOS0001'),
    'NEW MOTORHOME': ('c374ecca-e878-4204-9794-2fa69b3ca35f', 'BPOS0001'),
    'MOTORHOME_lt_36': ('24acfa8c-97b9-4e95-86de-d599fee69b4d', 'BPOS0002'),
    'MOTORHOME_mt_36': ('c9c45b09-1ce7-4f85-a95a-5473897714c7', 'BPOS0002'),
    '2nd_handCar_lt_36': ('6de4591f-9f05-419b-8f54-493e81da8eb8', 'BPOS0002'),
    '2dhCar_mt_36': ('20833d96-9285-430f-a01b-5dc4a74ab2c6', 'BPOS0002'),
    'RENOVATION': ('5527c48d-66ab-4a22-bd9d-b701e51b723d', 'BPOS0004'),
    'ENERGY': ('8d21a73b-d260-419d-b60d-06f852e6d5bd', 'BPOS0003')
}

def requestDataFor(creditType):
    url = "https://www.bpostbanque.be/bpb/content/atom/03c8f78e-d33a-47a5-9778-76ee8239a51c/content/data.json"

    querystring = {"id": loanTypes[creditType][0]}

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "7a1863df-881f-4d92-b71d-8bf52b0dcf32,a18ebb88-a006-4a90-99ad-7d3926837dcc",
        'Host': "www.bpostbanque.be",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)

def bankdata():
    bank_data = []
    for lType in loanTypes:
        data_for_type = []
        try :
            loanList = requestDataFor(lType)['Rates_infos']
        except:
            print("BPOST EXTENSION FOR {} IS ACTUALLY NOT AVAILABLE".format(lType))
            loanList = []
        for amtRange in loanList:
            for rate in amtRange['rates']:
                if rate['rate'] != 0:
                    data_for_type.append({'type': lType,
                                          'productID': loanTypes[lType][1],
                                          'duration': rate['duration'],
                                          'amount': amtRange['amountMin'],
                                          'amountMax': amtRange['amountMax'],
                                          'rate': rate['rate']})
        bank_data.append(data_for_type)
    return bank_data

def formatDataFromBank(bank_data, provider):
    frame_to_export = []
    for loanList in bank_data:
        for loan in loanList:
            frame_to_export.append([provider, loan['productID'], loan['type'], loan['amount'], loan['amountMax'],
                                    loan['duration'], loan['rate']])
    return frame_to_export


def bpostLoanScraper():
    print('BPOST LOAN SCRAPER PROCESSING ...')
    tab_col = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    return DataUtils.proc_data(bankdata(), 'BPOST', 'BPOST SCRAPE', 'bpost_rates', tab_col)


# bpostLoanScraper()








