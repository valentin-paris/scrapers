import requests
import json
import fileUtils
import DataUtils

loanTypes = {
    'PERSONAL LOAN': ('PL', 'EURO0001'),
    'NEW CAR LOAN': ('NW', 'EURO0002'),
    '2ND HAND CAR LOAN': ('TW', 'EURO003'),
    'OTHERS VEHICULES LOAN': ('AD', 'EURO004'),
    'RENOVATION LOAN': ('RL', 'EURO0004')
}

# loanRange = list(range(2500, 10000, 1000)) + list(range(10000, 30000, 2500)) + list(range(30000, 110000, 10000))
loanRange = [2500, 3000, 10000, 100000]
def makeRequestFor(lType, amount):
    #url = "https://www.europabank.be/WebsiteAPI/rest/loan/amounts"
    url = "blooops"

    querystring = {"type": loanTypes[lType][0], "bedrag": amount}

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "7839d327-280c-49bc-93f7-9a6bf8ea7fe5,66842b60-1f17-4db1-9270-0325557704bc",
        'Host': "www.europabank.be",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)

def addAttributes(loan, lType, amount, duration, rate):
        loan['type'] = lType
        loan['amount'] = amount
        loan['productID'] = loanTypes[lType][1]
        loan['rate'] = rate
        loan['duration'] = duration

def bankData():
    bankdata = []
    for ltype in loanTypes:
        data_for_type = []
        for amt in loanRange:
            try:
                loanList = makeRequestFor(ltype, amt)[0]['looptijd']
                for loan in loanList:
                    addAttributes(loan, ltype, amt, loan['maanden'], loan['jkp'])
                    data_for_type.append(loan)
            except:
                print('THE LINK {} FOR EUROPA BANK IS NOT AVAILABLE FOR THE MOMENT'.format(ltype))
                break
        bankdata.append(data_for_type) if data_for_type else bankdata + data_for_type
    return bankdata



def processData(dataMatrix, tab_Column, directoryName, fileName):
    fileUtils.displayRates(tab_Column, dataMatrix)
    return fileUtils.upToDate(fileName, directoryName, dataMatrix, tab_Column, [])

def europaLoanScraper():
    tab_col = ['PROVIDER ', 'PRODUCTID', 'LOAN TYPE', 'MIN AMT', 'MAX AMT', 'TERM', 'RATE']
    DataUtils.proc_data(bankData(), 'EUROPA BANK', 'EURO_BANK SCRAPE', 'euro_bank_rates', tab_col)






print(europaLoanScraper())


#print(makeRequestFor('new car', 2500))

# dataSample =[
#    {
#       "amount":19500,
#       "looptijd":[
#          {
#             "maanden":24,
#             "jkp":1.99,
#             "maandsom":829.30,
#             "totaal":19903.20,
#             "active":false,
#             "soort":"2",
#             "url":"https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000019500&jkp=01,99&soort=2&doel=NW"
#          },
#          {
#             "maanden":36,
#             "jkp":1.99,
#             "maandsom":558.29,
#             "totaal":20098.44,
#             "active":false,
#             "soort":"2",
#             "url":"https://www.europabank.be/apply-online/nl/autolening?lpt=036&bedrag=0000019500&jkp=01,99&soort=2&doel=NW"
#          },
#          {
#             "maanden":48,
#             "jkp":1.99,
#             "maandsom":422.82,
#             "totaal":20295.36,
#             "active":false,
#             "soort":"2",
#             "url":"https://www.europabank.be/apply-online/nl/autolening?lpt=048&bedrag=0000019500&jkp=01,99&soort=2&doel=NW"
#          },
#          {
#             "maanden":60,
#             "jkp":1.99,
#             "maandsom":341.55,
#             "totaal":20493,
#             "active":true,
#             "soort":"2",
#             "url":"https://www.europabank.be/apply-online/nl/autolening?lpt=060&bedrag=0000019500&jkp=01,99&soort=2&doel=NW"
#          },
#          {
#             "maanden":72,
#             "jkp":9.99,
#             "maandsom":356.94,
#             "totaal":25699.68,
#             "active":false,
#             "soort":"2",
#             "url":"https://www.europabank.be/apply-online/nl/autolening?lpt=072&bedrag=0000019500&jkp=09,99&soort=2&doel=NW"
#          },
#          {
#             "maanden":84,
#             "jkp":9.99,
#             "maandsom":319.31,
#             "totaal":26822.04,
#             "active":false,
#             "soort":"2",
#             "url":"https://www.europabank.be/apply-online/nl/autolening?lpt=084&bedrag=0000019500&jkp=09,99&soort=2&doel=NW"
#          }
#       ]
#    }
# ]

bs = [
   [
      {
         'maanden':12,
         'jkp':12.49,
         'maandsom':221.92,
         'totaal':2663.04,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=012&bedrag=0000002500&jkp=12,49&soort=3&doel=PL',
         'type':'personal loan',
         'amount':2500,
         'productID':'EURO0001',
         'rate':12.49,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':12.49,
         'maandsom':117.48,
         'totaal':2819.52,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=024&bedrag=0000002500&jkp=12,49&soort=3&doel=PL',
         'type':'personal loan',
         'amount':2500,
         'productID':'EURO0001',
         'rate':12.49,
         'duration':24
      },
      {
         'maanden':12,
         'jkp':12.49,
         'maandsom':266.3,
         'totaal':3195.6,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=012&bedrag=0000003000&jkp=12,49&soort=3&doel=PL',
         'type':'personal loan',
         'amount':3000,
         'productID':'EURO0001',
         'rate':12.49,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':12.49,
         'maandsom':140.98,
         'totaal':3383.52,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=024&bedrag=0000003000&jkp=12,49&soort=3&doel=PL',
         'type':'personal loan',
         'amount':3000,
         'productID':'EURO0001',
         'rate':12.49,
         'duration':24
      },
      {
         'maanden':30,
         'jkp':12.49,
         'maandsom':116,
         'totaal':3480,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=030&bedrag=0000003000&jkp=12,49&soort=3&doel=PL',
         'type':'personal loan',
         'amount':3000,
         'productID':'EURO0001',
         'rate':12.49,
         'duration':30
      },
      {
         'maanden':12,
         'jkp':9.99,
         'maandsom':877.11,
         'totaal':10525.32,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=012&bedrag=0000010000&jkp=09,99&soort=3&doel=PL',
         'type':'personal loan',
         'amount':10000,
         'productID':'EURO0001',
         'rate':9.99,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':9.99,
         'maandsom':459.42,
         'totaal':11026.08,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=024&bedrag=0000010000&jkp=09,99&soort=3&doel=PL',
         'type':'personal loan',
         'amount':10000,
         'productID':'EURO0001',
         'rate':9.99,
         'duration':24
      },
      {
         'maanden':30,
         'jkp':5.9,
         'maandsom':358.65,
         'totaal':10759.5,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=030&bedrag=0000010000&jkp=05,90&soort=3&doel=PL',
         'type':'personal loan',
         'amount':10000,
         'productID':'EURO0001',
         'rate':5.9,
         'duration':30
      },
      {
         'maanden':36,
         'jkp':4.9,
         'maandsom':298.78,
         'totaal':10756.08,
         'active':True,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=036&bedrag=0000010000&jkp=04,90&soort=3&doel=PL',
         'type':'personal loan',
         'amount':10000,
         'productID':'EURO0001',
         'rate':4.9,
         'duration':36
      },
      {
         'maanden':42,
         'jkp':4.9,
         'maandsom':259.1,
         'totaal':10882.2,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=042&bedrag=0000010000&jkp=04,90&soort=3&doel=PL',
         'type':'personal loan',
         'amount':10000,
         'productID':'EURO0001',
         'rate':4.9,
         'duration':42
      },
      {
         'maanden':48,
         'jkp':5.9,
         'maandsom':233.69,
         'totaal':11217.12,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=048&bedrag=0000010000&jkp=05,90&soort=3&doel=PL',
         'type':'personal loan',
         'amount':10000,
         'productID':'EURO0001',
         'rate':5.9,
         'duration':48
      },
      {
         'maanden':12,
         'jkp':9.99,
         'maandsom':8771.13,
         'totaal':105253.56,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=012&bedrag=0000100000&jkp=09,99&soort=3&doel=PL',
         'type':'personal loan',
         'amount':100000,
         'productID':'EURO0001',
         'rate':9.99,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':6.9,
         'maandsom':4463.26,
         'totaal':107118.24,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=024&bedrag=0000100000&jkp=06,90&soort=3&doel=PL',
         'type':'personal loan',
         'amount':100000,
         'productID':'EURO0001',
         'rate':6.9,
         'duration':24
      },
      {
         'maanden':36,
         'jkp':6.9,
         'maandsom':3073.6,
         'totaal':110649.6,
         'active':True,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=036&bedrag=0000100000&jkp=06,90&soort=3&doel=PL',
         'type':'personal loan',
         'amount':100000,
         'productID':'EURO0001',
         'rate':6.9,
         'duration':36
      },
      {
         'maanden':48,
         'jkp':6.9,
         'maandsom':2380.31,
         'totaal':114254.88,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=048&bedrag=0000100000&jkp=06,90&soort=3&doel=PL',
         'type':'personal loan',
         'amount':100000,
         'productID':'EURO0001',
         'rate':6.9,
         'duration':48
      },
      {
         'maanden':60,
         'jkp':6.9,
         'maandsom':1965.57,
         'totaal':117934.2,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=060&bedrag=0000100000&jkp=06,90&soort=3&doel=PL',
         'type':'personal loan',
         'amount':100000,
         'productID':'EURO0001',
         'rate':6.9,
         'duration':60
      },
      {
         'maanden':72,
         'jkp':9.99,
         'maandsom':1830.46,
         'totaal':131793.12,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=072&bedrag=0000100000&jkp=09,99&soort=3&doel=PL',
         'type':'personal loan',
         'amount':100000,
         'productID':'EURO0001',
         'rate':9.99,
         'duration':72
      },
      {
         'maanden':84,
         'jkp':9.99,
         'maandsom':1637.46,
         'totaal':137546.64,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=084&bedrag=0000100000&jkp=09,99&soort=3&doel=PL',
         'type':'personal loan',
         'amount':100000,
         'productID':'EURO0001',
         'rate':9.99,
         'duration':84
      },
      {
         'maanden':120,
         'jkp':9.99,
         'maandsom':1297.25,
         'totaal':155670,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/persoonlijke-lening?lpt=120&bedrag=0000100000&jkp=09,99&soort=3&doel=PL',
         'type':'personal loan',
         'amount':100000,
         'productID':'EURO0001',
         'rate':9.99,
         'duration':120
      }
   ],
   [
      {
         'maanden':24,
         'jkp':1.99,
         'maandsom':106.32,
         'totaal':2551.68,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000002500&jkp=01,99&soort=2&doel=NW',
         'type':'new car',
         'amount':2500,
         'productID':'EURO0002',
         'rate':1.99,
         'duration':24
      },
      {
         'maanden':24,
         'jkp':1.99,
         'maandsom':127.58,
         'totaal':3061.92,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000003000&jkp=01,99&soort=2&doel=NW',
         'type':'new car',
         'amount':3000,
         'productID':'EURO0002',
         'rate':1.99,
         'duration':24
      },
      {
         'maanden':24,
         'jkp':1.99,
         'maandsom':425.28,
         'totaal':10206.72,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000010000&jkp=01,99&soort=2&doel=NW',
         'type':'new car',
         'amount':10000,
         'productID':'EURO0002',
         'rate':1.99,
         'duration':24
      },
      {
         'maanden':36,
         'jkp':1.99,
         'maandsom':286.3,
         'totaal':10306.8,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=036&bedrag=0000010000&jkp=01,99&soort=2&doel=NW',
         'type':'new car',
         'amount':10000,
         'productID':'EURO0002',
         'rate':1.99,
         'duration':36
      },
      {
         'maanden':48,
         'jkp':1.99,
         'maandsom':216.83,
         'totaal':10407.84,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=048&bedrag=0000010000&jkp=01,99&soort=2&doel=NW',
         'type':'new car',
         'amount':10000,
         'productID':'EURO0002',
         'rate':1.99,
         'duration':48
      },
      {
         'maanden':24,
         'jkp':1.99,
         'maandsom':4252.8,
         'totaal':102067.2,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000100000&jkp=01,99&soort=2&doel=NW',
         'type':'new car',
         'amount':100000,
         'productID':'EURO0002',
         'rate':1.99,
         'duration':24
      },
      {
         'maanden':36,
         'jkp':1.99,
         'maandsom':2863.04,
         'totaal':103069.44,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=036&bedrag=0000100000&jkp=01,99&soort=2&doel=NW',
         'type':'new car',
         'amount':100000,
         'productID':'EURO0002',
         'rate':1.99,
         'duration':36
      },
      {
         'maanden':48,
         'jkp':1.99,
         'maandsom':2168.29,
         'totaal':104077.92,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=048&bedrag=0000100000&jkp=01,99&soort=2&doel=NW',
         'type':'new car',
         'amount':100000,
         'productID':'EURO0002',
         'rate':1.99,
         'duration':48
      },
      {
         'maanden':60,
         'jkp':1.99,
         'maandsom':1751.55,
         'totaal':105093,
         'active':True,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=060&bedrag=0000100000&jkp=01,99&soort=2&doel=NW',
         'type':'new car',
         'amount':100000,
         'productID':'EURO0002',
         'rate':1.99,
         'duration':60
      },
      {
         'maanden':72,
         'jkp':9.99,
         'maandsom':1830.46,
         'totaal':131793.12,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=072&bedrag=0000100000&jkp=09,99&soort=2&doel=NW',
         'type':'new car',
         'amount':100000,
         'productID':'EURO0002',
         'rate':9.99,
         'duration':72
      },
      {
         'maanden':84,
         'jkp':9.99,
         'maandsom':1637.46,
         'totaal':137546.64,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=084&bedrag=0000100000&jkp=09,99&soort=2&doel=NW',
         'type':'new car',
         'amount':100000,
         'productID':'EURO0002',
         'rate':9.99,
         'duration':84
      }
   ],
   [
      {
         'maanden':12,
         'jkp':12.49,
         'maandsom':221.92,
         'totaal':2663.04,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=012&bedrag=0000002500&jkp=12,49&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':2500,
         'productID':'EURO003',
         'rate':12.49,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':12.49,
         'maandsom':117.48,
         'totaal':2819.52,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000002500&jkp=12,49&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':2500,
         'productID':'EURO003',
         'rate':12.49,
         'duration':24
      },
      {
         'maanden':12,
         'jkp':12.49,
         'maandsom':266.3,
         'totaal':3195.6,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=012&bedrag=0000003000&jkp=12,49&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':3000,
         'productID':'EURO003',
         'rate':12.49,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':12.49,
         'maandsom':140.98,
         'totaal':3383.52,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000003000&jkp=12,49&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':3000,
         'productID':'EURO003',
         'rate':12.49,
         'duration':24
      },
      {
         'maanden':12,
         'jkp':9.99,
         'maandsom':877.11,
         'totaal':10525.32,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=012&bedrag=0000010000&jkp=09,99&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':10000,
         'productID':'EURO003',
         'rate':9.99,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':9.99,
         'maandsom':459.42,
         'totaal':11026.08,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000010000&jkp=09,99&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':10000,
         'productID':'EURO003',
         'rate':9.99,
         'duration':24
      },
      {
         'maanden':36,
         'jkp':4.9,
         'maandsom':298.78,
         'totaal':10756.08,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=036&bedrag=0000010000&jkp=04,90&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':10000,
         'productID':'EURO003',
         'rate':4.9,
         'duration':36
      },
      {
         'maanden':48,
         'jkp':5.9,
         'maandsom':233.69,
         'totaal':11217.12,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=048&bedrag=0000010000&jkp=05,90&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':10000,
         'productID':'EURO003',
         'rate':5.9,
         'duration':48
      },
      {
         'maanden':12,
         'jkp':9.99,
         'maandsom':8771.13,
         'totaal':105253.56,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=012&bedrag=0000100000&jkp=09,99&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':100000,
         'productID':'EURO003',
         'rate':9.99,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':6.9,
         'maandsom':4463.26,
         'totaal':107118.24,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000100000&jkp=06,90&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':100000,
         'productID':'EURO003',
         'rate':6.9,
         'duration':24
      },
      {
         'maanden':36,
         'jkp':6.9,
         'maandsom':3073.6,
         'totaal':110649.6,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=036&bedrag=0000100000&jkp=06,90&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':100000,
         'productID':'EURO003',
         'rate':6.9,
         'duration':36
      },
      {
         'maanden':48,
         'jkp':6.9,
         'maandsom':2380.31,
         'totaal':114254.88,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=048&bedrag=0000100000&jkp=06,90&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':100000,
         'productID':'EURO003',
         'rate':6.9,
         'duration':48
      },
      {
         'maanden':60,
         'jkp':6.9,
         'maandsom':1965.57,
         'totaal':117934.2,
         'active':True,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=060&bedrag=0000100000&jkp=06,90&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':100000,
         'productID':'EURO003',
         'rate':6.9,
         'duration':60
      },
      {
         'maanden':72,
         'jkp':9.99,
         'maandsom':1830.46,
         'totaal':131793.12,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=072&bedrag=0000100000&jkp=09,99&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':100000,
         'productID':'EURO003',
         'rate':9.99,
         'duration':72
      },
      {
         'maanden':84,
         'jkp':9.99,
         'maandsom':1637.46,
         'totaal':137546.64,
         'active':False,
         'soort':'2',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=084&bedrag=0000100000&jkp=09,99&soort=2&doel=TW',
         'type':'2nd hand car',
         'amount':100000,
         'productID':'EURO003',
         'rate':9.99,
         'duration':84
      }
   ],
   [
      {
         'maanden':12,
         'jkp':12.49,
         'maandsom':221.92,
         'totaal':2663.04,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=012&bedrag=0000002500&jkp=12,49&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':2500,
         'productID':'EURO004',
         'rate':12.49,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':12.49,
         'maandsom':117.48,
         'totaal':2819.52,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000002500&jkp=12,49&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':2500,
         'productID':'EURO004',
         'rate':12.49,
         'duration':24
      },
      {
         'maanden':12,
         'jkp':12.49,
         'maandsom':266.3,
         'totaal':3195.6,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=012&bedrag=0000003000&jkp=12,49&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':3000,
         'productID':'EURO004',
         'rate':12.49,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':12.49,
         'maandsom':140.98,
         'totaal':3383.52,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000003000&jkp=12,49&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':3000,
         'productID':'EURO004',
         'rate':12.49,
         'duration':24
      },
      {
         'maanden':12,
         'jkp':9.99,
         'maandsom':877.11,
         'totaal':10525.32,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=012&bedrag=0000010000&jkp=09,99&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':10000,
         'productID':'EURO004',
         'rate':9.99,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':9.99,
         'maandsom':459.42,
         'totaal':11026.08,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000010000&jkp=09,99&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':10000,
         'productID':'EURO004',
         'rate':9.99,
         'duration':24
      },
      {
         'maanden':36,
         'jkp':4.9,
         'maandsom':298.78,
         'totaal':10756.08,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=036&bedrag=0000010000&jkp=04,90&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':10000,
         'productID':'EURO004',
         'rate':4.9,
         'duration':36
      },
      {
         'maanden':48,
         'jkp':5.9,
         'maandsom':233.69,
         'totaal':11217.12,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=048&bedrag=0000010000&jkp=05,90&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':10000,
         'productID':'EURO004',
         'rate':5.9,
         'duration':48
      },
      {
         'maanden':12,
         'jkp':9.99,
         'maandsom':8771.13,
         'totaal':105253.56,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=012&bedrag=0000100000&jkp=09,99&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':100000,
         'productID':'EURO004',
         'rate':9.99,
         'duration':12
      },
      {
         'maanden':24,
         'jkp':6.9,
         'maandsom':4463.26,
         'totaal':107118.24,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=024&bedrag=0000100000&jkp=06,90&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':100000,
         'productID':'EURO004',
         'rate':6.9,
         'duration':24
      },
      {
         'maanden':36,
         'jkp':6.9,
         'maandsom':3073.6,
         'totaal':110649.6,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=036&bedrag=0000100000&jkp=06,90&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':100000,
         'productID':'EURO004',
         'rate':6.9,
         'duration':36
      },
      {
         'maanden':48,
         'jkp':6.9,
         'maandsom':2380.31,
         'totaal':114254.88,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=048&bedrag=0000100000&jkp=06,90&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':100000,
         'productID':'EURO004',
         'rate':6.9,
         'duration':48
      },
      {
         'maanden':60,
         'jkp':6.9,
         'maandsom':1965.57,
         'totaal':117934.2,
         'active':True,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=060&bedrag=0000100000&jkp=06,90&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':100000,
         'productID':'EURO004',
         'rate':6.9,
         'duration':60
      },
      {
         'maanden':72,
         'jkp':9.99,
         'maandsom':1830.46,
         'totaal':131793.12,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=072&bedrag=0000100000&jkp=09,99&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':100000,
         'productID':'EURO004',
         'rate':9.99,
         'duration':72
      },
      {
         'maanden':84,
         'jkp':9.99,
         'maandsom':1637.46,
         'totaal':137546.64,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/autolening?lpt=084&bedrag=0000100000&jkp=09,99&soort=3&doel=AD',
         'type':'others vehicules',
         'amount':100000,
         'productID':'EURO004',
         'rate':9.99,
         'duration':84
      }
   ],
   [
      {
         'maanden':13,
         'jkp':4.2,
         'maandsom':196.96,
         'totaal':2560.48,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=013&bedrag=0000002500&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':2500,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':13
      },
      {
         'maanden':24,
         'jkp':4.2,
         'maandsom':108.7,
         'totaal':2608.8,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=024&bedrag=0000002500&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':2500,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':24
      },
      {
         'maanden':13,
         'jkp':4.2,
         'maandsom':236.36,
         'totaal':3072.68,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=013&bedrag=0000003000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':3000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':13
      },
      {
         'maanden':24,
         'jkp':4.2,
         'maandsom':130.44,
         'totaal':3130.56,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=024&bedrag=0000003000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':3000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':24
      },
      {
         'maanden':13,
         'jkp':4.2,
         'maandsom':787.85,
         'totaal':10242.05,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=013&bedrag=0000010000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':10000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':13
      },
      {
         'maanden':24,
         'jkp':4.2,
         'maandsom':434.79,
         'totaal':10434.96,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=024&bedrag=0000010000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':10000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':24
      },
      {
         'maanden':36,
         'jkp':4.2,
         'maandsom':295.78,
         'totaal':10648.08,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=036&bedrag=0000010000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':10000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':36
      },
      {
         'maanden':48,
         'jkp':4.2,
         'maandsom':226.33,
         'totaal':10863.84,
         'active':True,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=048&bedrag=0000010000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':10000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':48
      },
      {
         'maanden':13,
         'jkp':4.2,
         'maandsom':7878.5,
         'totaal':102420.5,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=013&bedrag=0000100000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':100000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':13
      },
      {
         'maanden':24,
         'jkp':4.2,
         'maandsom':4347.89,
         'totaal':104349.36,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=024&bedrag=0000100000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':100000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':24
      },
      {
         'maanden':36,
         'jkp':4.2,
         'maandsom':2957.8,
         'totaal':106480.8,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=036&bedrag=0000100000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':100000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':36
      },
      {
         'maanden':48,
         'jkp':4.2,
         'maandsom':2263.34,
         'totaal':108640.32,
         'active':True,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=048&bedrag=0000100000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':100000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':48
      },
      {
         'maanden':60,
         'jkp':4.2,
         'maandsom':1847.13,
         'totaal':110827.8,
         'active':False,
         'soort':'3',
         'url':'https://www.europabank.be/apply-online/nl/renovatielening?lpt=060&bedrag=0000100000&jkp=04,20&soort=3&doel=RL',
         'type':'renovation',
         'amount':100000,
         'productID':'EURO0004',
         'rate':4.2,
         'duration':60
      }
   ]
]