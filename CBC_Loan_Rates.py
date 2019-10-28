import requests
import json
# import fileUtils
import DataUtils

url = "https://www.cbc.be/PSA/A058/service/calculateLoanSimulation/1"

querystring = {"cb":"1565018047681"}

headers = {
    'Accept': "application/json",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    'company': "0002",
    'Connection': "keep-alive",
    'Content-Length': "186",
    'Content-Type': "application/json;charset=UTF-8",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Cache-Control': "no-cache",
    'Postman-Token': "7f690e00-dacd-43b6-a467-773e01bd974c,4ef77785-5647-4f80-adfa-630a5b1336ce",
    'Host': "www.cbc.be",
    'Cookie': "PSASESSIONID=AAC0D685D775F9D4F5310C3EA71FA871.1; TS015834e9=01998c50f2476b29ba9c14abbf8f2021528adedeb2f6b6a6d701478385ec12c5b57f18ece7f7a9f5572bce3c1bf250f2061fd498bc058dbfc1708d955d7a9712fdea9dcee79dda707721a559292f15618074f0606a617e48f7254a5889429aef234b987b264ddf770982cb375f789513a6b9ea957c4db481f590c3ca722ded42206fd496732107ba6743c8f64d37da95278695ebdf; sat_track=true; TS0127c266=01998c50f2902f26813df43ea273eea35760806f3130619ae7ca37ac4dcceee49907fccbbdbe33b856d799ebfe84cf18a5eed920ef886c50252775d8a6c34f1590b97bc880fb9f763b80ad7996646cbe9d7a4360e4ce427d80683a80d7ff3f2b873b47125ea79347d304bcf00f69b59ef3ca680b91; PD_STATEFUL_78a410d6-37ca-11e9-8a4c-005056864a2c=%2FPSA; PD_STATEFUL_86b729b0-37ca-11e9-8a4c-005056864a2c=VHWWWCBCBE; PD_STATEFUL_863cdc9a-30a5-11e9-bf0b-00505686a95a=%2FPSA; PD_STATEFUL_005d13d0-30ad-11e9-b67a-00505683782b=%2FPSA; TS011f471c=01998c50f2e1bc4496f7e8cf4d24cafdb96d9160ac2730728beea89b054daeb8ad31c39cf838a716a3c9679e2355bbdc66f8cbd3f865bddba0ecbf5e2184cac4673b7f0b1e5924d2fdbc277542e7484a46714553efc8171b6ca10809ded3c477da4d563bac81417700d7a17e8b5b778d44ed05db217fa4dd6883a0821e08ef2ec5dadb296c",
    'cache-control': "no-cache"
    }


#loan types and their codes for the requests
loanTypes = {
    'Prêt Voiture Neuve': ('80301', 'CBCX0001'),
    'Prêt Voiture d\'occasion': ('80303', 'CBCX0002'),
    'Prêt Rénovation': ('60290', 'CBCX0003'),
    'Prêt Personnel': ('30096', 'CBCX0004'),
    'Prêt Energie': ('60293', 'CBCX0005')
}

amntToMonthRanges = {
    tuple(range(2500, 4000, 500)): list(range(12, 36, 6)),
    tuple(range(4000, 6000, 500)): list(range(12, 42, 6)),
    tuple(range(6000, 8000, 500)): list(range(12, 48, 6)),
    tuple(range(8000, 11000, 1000)): list(range(12, 54, 6)),
    tuple(range(11000, 16000, 1000)): list(range(12, 66, 6)),
    tuple(range(17000, 27000, 2000)): list(range(12, 78, 6))
}

def makeDataRequestFor(amount, category, duration):
    payload = {"creditPurposeCode": {"T": "text", "V": loanTypes[category][0]},
                "loanAmount": {"V": str(amount), "T": "decimal"},
                "maturityMonthQuantity": {"V": str(duration), "E": "XMADg6Dx/ncBfdlwyFI17+ULAZ/s6bUBdZqZ0kt2bcA=", "T": "decimal"}}
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    return json.loads(response.text[6:])

def bank_data():
    structuredData = []
    print('CBC LOAN SCRAPE PROCESSING ', end='')
    for category in loanTypes:
        for amtRange in amntToMonthRanges:
            for amount in amtRange:
                ratePerMonth = []
                for duration in amntToMonthRanges[amtRange]:
                    print('.', end='')
                    try:
                        dataForAmtAndDuration = makeDataRequestFor(amount, category, duration)
                    except:
                        print(amount)
                        print(duration)
                        print(category)
                        dataForAmtAndDuration = None

                    if dataForAmtAndDuration:
                        dataForAmtAndDuration['type'] = category
                        dataForAmtAndDuration['amount'] = amount
                        dataForAmtAndDuration['duration'] = duration
                        dataForAmtAndDuration['rate'] = dataForAmtAndDuration['personalProperty']['yearInterestPercent']['V']
                        dataForAmtAndDuration['productID'] = loanTypes[category][1]
                        ratePerMonth.append(dataForAmtAndDuration)
                structuredData.append(ratePerMonth)
        print()
    return structuredData

def createGroups(structuredData):
    loanGroups = {}
    for loanList in structuredData:
        for loanElement in loanList:
            if (loanElement['type'], loanElement['duration'], loanElement['rate'], loanElement['productID']) not in loanGroups.keys():
                loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'], loanElement['productID'])]\
                    = [loanElement['amount']]
            else:
                loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'], loanElement['productID'])]\
                    .append(loanElement['amount'])
    return loanGroups

def formatDataFrom(groups, provider):
    frameToExport = []
    for eachGroup in groups:
        frameToExport.append([provider, eachGroup[3], eachGroup[0], min(map(float, groups[eachGroup])),
                              max(map(float, groups[eachGroup])), int(eachGroup[1]), float(eachGroup[2])])
    return frameToExport

def cbcLoanScraper():
    cbcBankData = bank_data()
    tab_Column = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    return DataUtils.proc_data(cbcBankData, 'CBC BANK', 'CBC BANK SCRAPING', 'CBC LOANS', tab_Column)


# cbcLoanScraper()








