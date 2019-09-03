import requests
import re

url = "https://www.bnpparibasfortis.be/site/renderers/empty.aspx"

querystring = {"ID":"pAsqJEdzpk9nkU0L079uvijIirnUKMeCkrFjEL9XxlmIIN%2B3pGWB6CO2qO7yaFlc6NsEXIyW6adCpM_Hy_nLo2KlpL","CREDIT_AIM":"214","BEDRAG":"15000","REIMBURSEMENT_MODE":"1"}

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

print(response.text)
print(type(response.text))

txt = response.text

pat = ('\|\|.*\|\|')

x = re.search(pat, txt)
if (x):
  print("YES! We have a match!")
  print(x)
  print(x.group(0))

else:
  print("No match")

# for el in txt:
#     print(el)



