import requests
import json
import DataUtils



loanTypes = {
    "renovation": {
        "productID": "SANT0003",
        "index": 1
    },
    "personal": {
        "productID": "SANT0001",
        "index": 8
    }
}


range_for_loan = {
    tuple(list(range(600, 1200, 200))): [12],
    tuple(list(range(1200, 5400, 1000))): [12, 24],
    tuple(list(range(6000, 20000, 1500))): [12, 24, 36, 48, 60],
    tuple(list(range(20000, 52500, 25500))): [12, 24, 36, 48, 60, 72]
}


def requestDataFor(lType, amount, monthPayment):
    url = "https://www.santander.be/Calculate/CalculateInstallment/"

    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
    }

    payload = {
        "CalculationType": 1,
        "ProductType": 2,
        "LoanAmount": amount,
        "MonthAmount": monthPayment,
        "SelectedOptionIndex": loanTypes[lType]["index"],
        "UmbracoNodeId": 1282}
    response = requests.request("POST", url, json=payload, headers=headers)
    try:
        return json.loads(response.text)
    except:
        return {}


def data_for_type(lType):
    data_for_type = []
    for key in range_for_loan:
        for amt in key:
            for term in range_for_loan[key]:
                print(".", end="")
                try :
                    loanList = requestDataFor(lType, amt, amt/term)["CalculatedInstallmentOptions"]
                except:
                    loanList = []
                for loanJson in loanList:
                    loan = {
                        "type" : lType,
                        "productID": loanTypes[lType]["productID"],
                        "amount": loanJson["LoanAmount"],
                        "duration": loanJson["Term"],
                        "rate": loanJson["AnnualPercentageRate"] if loanJson["AnnualPercentageRate"] != 0 else
                        loanJson["InterestRate"]
                    }
                    if loan not in data_for_type:
                        data_for_type.append(loan)
    print()
    if not data_for_type:
        print("THE EXTENSION {} LOANS FOR SANTANDER IS NOT AVAILABLE.".format(lType.upper()))
        print()
    return data_for_type


def loanProceduree(lType):
    print("SANTANDER {} LOANS SCRAPE PROCESSING ...".format(lType.upper()))
    bank_data = [data_for_type(lType)]
    tab_col = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    return DataUtils.proc_data(bank_data, "SANTANDER", "SANTANDER SCRAPE", "santander_{}_loans_rates".format(lType), tab_col)

def santanderLoanScraper():
    result = []
    for lType in loanTypes:
        result += loanProceduree(lType)
    return result



# santanderLoanScraper()