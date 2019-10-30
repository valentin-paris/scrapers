import requests
import fileUtils

prodctTypes = {
    "PERSONAL LOAN": {
        "code": "140",
        "product_ID": "BNPF0003"
    },
    "RENOVATION LOAN": {
        "code":"116",
        "product_ID": "BNPF0001"
    },
    "NEW CAR LOAN": {
        "code": "246",
        "product_ID": "BNPF0003"
    },
    "NEW_MOTO_OR_QUAD": {
        "code": "246",
        "product_ID": "BNPF0003"
    },
    "NEW MOBIL_HOME": {
        "code": "229",
        "product_ID": "BNPF0003"
    },
    "NEW ECO_CAR":{
        "code": "216",
        "product_ID": "BNPF0008"
    },
    "SOFT_MOBILITY_NEW": {
        "code": "246",
        "product_ID": "BNPF0003"
    },
    "CAR_LT_3Y": {
        "code": "215",
        "product_ID": "BNPF0005"
    },
    "CAR_MT_3Y": {
        "code": "214",
        "product_ID": "BNPF0005"
    },
    "MOB_HOM_MT_3Y": {
        "code": "221",
        "product_ID": "BNPF0005"
    },
    "MOB_HOM_LT_3Y": {
        "code": "214",
        "product_ID": "BNPF0005"
    },
    "LT_3Y_MOTO_SCOOTER": {
        "code": "262",
        "product_ID": "BNPF0005"
    },
    "MT_3Y_MOTO_SCOOTER": {
        "code": "255",
        "product_ID": "BNPF0005"
    },
    "NRG_ISOLATION": {
        "code": "228",
        "product_ID": "BNPF0002"
    },
    "NRG_HAETING": {
        "code": "232",
        "product_ID": "BNPF0002"
    },
    "NRG_DBL_WINDOW": {
        "code": "241",
        "product_ID": "BNPF0002"
    },
    "SOLAR_NRG": {
        "code": "242",
        "product_ID": "BNPF0002"
    },
    "NRG_OTHERS": {
        "code": "243",
        "product_ID": "BNPF0002"
    },
    "GEOTHERMAL_HEATING": {
        "code": "237",
        "product_ID": "BNPF0002"
    },
    "ECO_NRG_VENTILATION": {
        "code": "247",
        "product_ID": "BNPF0002"
    },
}

amountRange = [2500, 5000, 10000, 15000, 20000, 30000]

def makeRequestFor(pdType, amount):
    url = "https://www.bnpparibasfortis.be/site/renderers/empty.aspx"

    querystring = {
                        "ID": "pAsqJEdzpk9nkU0L079uvijIirnUKMeCkrFjEL9XxlmIIN%2B3pGWB6CO2qO7yaFlc6NsEXIyW6adCpM_Hy_nLo2KlpL",
                       "CREDIT_AIM": prodctTypes[pdType]['code'],
                       "BEDRAG": amount,
                       "REIMBURSEMENT_MODE": "1"
                   }

    headers = {
        'User-Agent': "PostmanRuntime/7.16.3",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "408bdee9-9986-4141-beb7-e9319e9eaa1e,6c30089c-e94a-4740-a181-40feb0e8883c",
        'Host': "www.bnpparibasfortis.be",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text.split('||')

def bankData():
    bank_data = []
    for pdt in prodctTypes:
        data_for_type = []
        for amount in amountRange:
            loanList = makeRequestFor(pdt, amount)
            for loan in loanList:
                if loan:
                    loan_data = loan.split('|')
                    loan_data[3] = '50000' if int(loan_data[3]) > 50000 else loan_data[3]
                    loan_data[1] = '-' if int(loan_data[1]) > 120 else loan_data[1]
                    try:
                        taux = float(loan_data[4][:4])
                    except:
                        taux = float(loan_data[4][:3])
                    data_for_type.append(dict(amount=loan_data[2], type=pdt, productID=prodctTypes[pdt]["product_ID"],
                                              maxAmnt=loan_data[3],rate=taux, duration=int(loan_data[0]),
                                              maxDuration=loan_data[1]))
        bank_data.append(data_for_type)
    return bank_data

def formatDataFromBank(bank_data, provider):
    frame_to_export = []
    for loanList in bank_data:
        for loan in loanList:
            frame_to_export.append([provider, loan['productID'], loan['type'], loan['amount'], loan['maxAmnt'],
                                    loan['duration'], loan['maxDuration'], loan['rate']])
    return frame_to_export

# def bnpLoanScraper():
#     print('BNP SCRAPE PROCESSING ...')
#     tab_col = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'MINTERM','MAXTERM' , 'RATE']
#     data_matrix = formatDataFromBank(bankData(), 'BNP')
#     if data_matrix:
#         fileUtils.displayRates(tab_col, data_matrix)
#         return fileUtils.upToDate('bnp_rates', 'BNP SCRAPE', data_matrix, tab_col, [])
#     else:
#         return None

#for testing purposes another way to store the rate may be better

def pdt_bank_data(product):
    data_for_type = []
    for amount in amountRange:
        loanList = makeRequestFor(product, amount)
        for loan in loanList:
            if loan:
                loan_data = loan.split('|')
                loan_data[3] = '50000' if int(loan_data[3]) > 50000 else loan_data[3]
                loan_data[1] = '-' if int(loan_data[1]) > 120 else loan_data[1]
                try:
                    taux = float(loan_data[4][:4])
                except:
                    taux = float(loan_data[4][:3])
                data_for_type.append(dict(amount=float(loan_data[2]), type=product, productID=prodctTypes[product]["product_ID"],
                                          maxAmnt=float(loan_data[3]),rate=taux, duration=int(loan_data[0]),
                                          maxDuration=loan_data[1]))
    return [data_for_type]

def loanProcedure(pdt):
    print('BNPPF {} SCRAPE PROCESSING ...'.format(pdt))
    tab_col = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'MINTERM','MAXTERM' , 'RATE']
    data_matrix = formatDataFromBank(pdt_bank_data(pdt), 'BNPPF')
    if data_matrix:
        fileUtils.displayRates(tab_col, data_matrix)
        return fileUtils.upToDate('bnp_{}_rates'.format(pdt.lower()), 'BNP SCRAPE', data_matrix, tab_col)
    else:
        return None

def scraper():
    result = []
    for pdt in prodctTypes:
       result += loanProcedure(pdt)
    return result

#use the scraper method to run the scraper
# scraper()








