import requests, json
import fileUtils



'''
        REQUEST PARAMETERS 
'''
cookies = {
    'JSESSIONID': 'p27NP_x_iFHH97ytbEWyPo_43v3YBHCJ3bc9bzv8.buywl0004:phenix-buywl0004',
    'TS0181821e': '016b073a45469bd8f301524540984217e0ea18c14a4992892bab94a3e2c58747cbc90046c8799c2e750301f979c5c6b0dc72d5b3b1acf6da9db349a3e0aa2478417706a438',
    'BIGipServer~ap-buyway_int_app_front_dmz-337~p-buyway-phenix-front-prod-80': 'rd337o00000000000000000000ffff0ad7b544o80',
    'TS016b11db': '016b073a45172d4b659098f0e10328a38f4777e14058492e8dc3a1dd65b1c0cc6002cb00040515baff2e19b9342b6330d3ddc7c12a46af5ee7e64e3a6dda5e023af04d8bbd',
}

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://loan.carrefourfinance.be',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.36',
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
}

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


'''
Data structure description
at first level, we have a dictionnary with 2 elements and the second containing the core data
the 2nd element is also a dictionnary and the key containing rates is key = state
'''

'''
    GLOBAL VARIABLES 
'''
# directory = 'Carrefour Finance loans'
directory = 'Carrefour Finance Loans'
colonnes = ['PROVIDER', 'CATEGORY', 'LOAN FROM', 'TO', 'MIN TERM', 'MAX TERM', 'RATE']
response = requests.post('https://loan.carrefourfinance.be/fimsim/', headers=headers, params=params, cookies=cookies, data=data)
# print(type(json.loads(response.content)))
print(json.loads(response.content))


def requestData():
    listOfElements = []
    #extraction of all the potential usefull data from json to python dict  in a list a list
    for elt in json.loads(response.content):
        try:
            val = json.loads((json.loads(response.content)[elt]))
            listOfElements.append(val)
            return listOfElements
        except:
            pass

#valuable data is a dictionnary made up of two elements key 0 with the htmlPge attributes details
#and key 1 with the loan rates details
def getValuableData(listOfObj):
    for jsObject in listOfObj:
        for key in jsObject:
            if key == 'state':
                return jsObject[key]

#the rates are structured as dictionnary and the key with the value of full content of rates value is 'materialCodesMapping'
def allRates(valuabData):
    return valuabData['1']["materialCodesMapping"]

#returns the value of key rateRanges that is a list of list rates
def rateList(rates):
    rList = []
    for i in range(len(rates[1])):
        rList.append(rates[1][i]['rateRanges'])
    return rList

#returns the data to be monitored for all rates categories
def trackableData(rates):
    provider = "CARREFOUR FINANCE"
    rawContent = []
    rList = rateList(rates)
    for i in range(len(rates[0])):
        for j in range(len(rList)):
            rawContent.append([provider, rates[0][i]['label'], rList[i][j]['minCreditAmount'], rList[i][j]['maxCreditAmount'], rList[i][j]['minDuration'], rList[i][j]['maxDuration'], rList[i][j]['taeg']])
    return rawContent

#defines the procedure for each rate categry in parameter
def loanProcedure(loanCategoryFr, nlLoanCtagory):
    loans = allRates(getValuableData(requestData()))
    provider = 'CARREFOUR FINANCE'
    rawContent = []
    rList = rateList(loans)
    for i in range(len(loans[0])):
        if loans[0][i]['label'] == loanCategoryFr or loans[0][i]['label'] == nlLoanCtagory:
            for j in range(len(rList)):
                rawContent.append(
                    [provider, loans[0][i]['label'], rList[i][j]['minCreditAmount'], rList[i][j]['maxCreditAmount'],
                     '{} {}'.format(rList[i][j]['minDuration'], ' Months'), '{} {}'.format(rList[i][j]['maxDuration'], 'Months'), '{} {}'.format(rList[i][j]['taeg'], '%')])
    fileUtils.displayRates(colonnes, rawContent)
    fileUtils.upToDate(nlLoanCtagory, directory, rawContent, colonnes)
    return rawContent




def secondHaandcarLoan():
    loanProcedure('Véhicule d\'occasion', 'Tweedehands voertuig' )

def newCarLoan():
    loanProcedure('Véhicule neuf', 'Nieuw voertuig')

def renovationloan():
    loanProcedure('Travaux / Déco', 'Werken')


# renovationloan()
#
# newCarLoan()
# #
# secondHaandcarLoan()
# fileUtils.displayRates(colonnes, trackableData(allRates(getValuableData(requestData()))))


raw_cont = [
                ['CARREFOUR FINANCE', 'Travaux / Déco', '6000', '7500', '6  Months', '6 Months', '8.9 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '10000.01', '15000', '6  Months', '6 Months', '8.9 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '10000.01', '15000', '43  Months', '60 Months', '5.9 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '10000.01', '15000', '7  Months', '30 Months', '5.4 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '20000.01', '40000', '61  Months', '84 Months', '6.9 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '3700', '3700', '6  Months', '30 Months', '8.9 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '6000', '7500', '31  Months', '42 Months', '4.49 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '7500.01', '10000', '43  Months', '48 Months', '5.9 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '15000.01', '20000', '31  Months', '42 Months', '4.49 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '15000.01', '20000', '61  Months', '84 Months', '6.9 %'],
                ['CARREFOUR FINANCE', 'Travaux / Déco', '3700.01', '5600', '6  Months', '36 Months', '8.9 %']
]









