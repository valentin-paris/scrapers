import requests
import json
import DataUtils
import fileUtils

axaLoanTypes = {
    'new car': {
        'level1': 39,
        'level2': 42,
        'level3': 48,
        'productID': 'AXAB0001'
    },
    '2nd_hand_car_lt_6month': {
        'level1': 39,
        'level2': 42,
        'level3': 49,
        'productID': 'AXAB0001'
    },
    '2nd_hand_car_btn_6M_to_3Y': {
        'level1': 39,
        'level2': 42,
        'level3': 50,
        'productID': 'AXAB0002'
    },
    '2nd_hand_car_btn_3Y_to_5Y': {
        'level1': 39,
        'level2': 42,
        'level3': 52,
        'productID': 'AXAB0002'
    },
    'new_motobike': {
        'level1': 39,
        'level2': 43,
        'level3': 51,
        'productID': 'AXAB0002'
    },
    'motobike_lt_3Y': {
        'level1': 39,
        'level2': 43,
        'level3': 51,
        'productID': 'AXAB0002'
    },
    'motobike_btn_3Y_to_5y': {
        'level1': 39,
        'level2': 43,
        'level3': 52,
        'productID': 'AXAB0002'
    },
    'new mobilhome': {
        'level1': 39,
        'level2': 44,
        'level3': 48,
        'productID': 'AXAB0006'
    },
    'mobilhome_2nd_hand_lt_3Y': {
        'level1': 39,
        'level2': 44,
        'level3': 51,
        'productID': 'AXAB0006'
    },
    '2nd_hand_mobilhome_btn_3Y_to_5Y': {
        'level1': 39,
        'level2': 44,
        'level3': 52,
        'productID': 'AXAB0006'
    },
    'other_car_new': {
        'level1': 39,
        'level2': 45,
        'level3': 48,
        'productID': 'AXAB0001'
    },
    'other_car_2nd_hand_lt_3Y': {
        'level1': 39,
        'level2': 45,
        'level3': 51,
        'productID': 'AXAB0002'
    },
    'other_car_2nd_hand_3Y_to_5Y': {
        'level1': 39,
        'level2': 45,
        'level3': 52,
        'productID': 'AXAB0002'
    },
    'energy loan': {
        'level1': 40,
        'level2': 47,
        'level3': 0,
        'productID': 'AXAB0004'
    },
    'renovation loan': {
        'level1': 40,
        'level2': 46,
        'level3': 0,
        'productID': 'AXAB0003'
    },
    'personal loan': {
        'level1': 41,
        'level2': 0,
        'level3': 0,
        'productID': 'AXAB0005'
    },

}

amountRanges = list(range(2500, 15000, 1000)) + list(range(15000, 30000, 2500)) + list(range(30000, 75000, 10000))

#request for data
def makeRequestFor(lType, amount):
    url = "https://www.axabank.be/Webservices/LoanSimulatorService.asmx/Simulate"
    payload = {
        "level1": axaLoanTypes[lType]['level1'],
        "level2": axaLoanTypes[lType]['level2'],
        "level3": axaLoanTypes[lType]['level3'],
        "duration": "",
        "monthlyAmount": 275,
        "total": amount,
        "variableAmount": 0,
        "isMonthly": None,
        "lang": "fr"
    }
    response = requests.request("POST", url, json=payload)
    return json.loads(response.text)


def bankData():
    bankdata = []
    for lType in axaLoanTypes:
        loan_type_data = []
        for amt in amountRanges:
            print('.', end='')
            loanList = makeRequestFor(lType, amt)['d']['CarouselItems']
            for loan in loanList:
                loan['type'] = lType
                loan['duration'] = loan['Duration']
                loan['rate'] = loan['Jkp']
                loan['productID'] = axaLoanTypes[lType]['productID']
                loan['amount'] = loan['RequestAmount']
                loan_type_data.append(loan)
        bankdata.append(loan_type_data)
        print()
    return bankdata


def axaLoanScraper():
    print('AXA LOAN SCRAPER PROCESSING ')
    tab_Column = ['PROVIDER ', 'PRODUCT_ID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    dataMatrix = DataUtils.formatDataFrom(DataUtils.createGroups(bankData()), 'AXA_BANK')
    return DataUtils.processData(dataMatrix, tab_Column, 'AXA SCRAPE', 'axa_rates')

#axaLoanScraper()









