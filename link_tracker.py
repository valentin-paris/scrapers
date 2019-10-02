import requests
from bs4 import BeautifulSoup
from fileUtils import no_double
import json
import fileUtils



mailList = ['alerts@topcompare.be', 'quentin@topcompare.be', "bernaud.toukam@topcompare.be"]
mailTest = ["bernaud.toukam@topcompare.be"]
def get_links_from_website():
    link_list = []
    tc_personal_loan_url = "https://www.topcompare.be/api/personal-loan/v2/products"

    querystring = {
                    "journeyId": "01007747-c4dd-49a2-a89c-3ea493674bde",
                    "category": "personalLoan",
                    "wantToBorrow": "8000",
                    "wantToBorrowTime": "48",
                    "wantToBorrowTimeUnit": "month"
                   }

    response = requests.request("GET", tc_personal_loan_url, params=querystring)

    soup = BeautifulSoup(response.text, "html.parser")

    btn_list = soup.find_all("button")

    for i in range(len(btn_list)):
        if "data-url" in btn_list[i].attrs:
            link_list.append({"id": btn_list[i].attrs["data-cgg-id"], "link": btn_list[i].attrs["data-url"]})
    return no_double(link_list)

def api_links():
    url = "https://www.topcompare.be/api/personal-loan/v2/loans/personalLoan"

    querystring = {"backendRendering": "false", "journeyId": "3248cdbf-ad5f-443f-ae47-6d021c623f64",
                   "sortBy": ["mrp%2B", "apr%2B", "trp%2B"], "wantToBorrow": "9233", "wantToBorrowTime": "36",
                   "wantToBorrowTimeUnit": "month", "lang": "fr", "pageSize": "15"}
    response = requests.request("GET", url, params=querystring)

    return (json.loads(response.text)["products"])

def construct_link(web_link):
    return "https://www.topcompare.be{}".format(web_link)

def is_link_functional(link):
    try:
        return requests.request("GET", link).status_code == 200
    except:
        try:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            return requests.request("GET", link, verify=False).status_code == 200
        except:
            return False

def check_links():
    print("checking the links ...")
    general_message = []
    for product in get_links_from_website():
        for api_product in api_links():
            if product["id"] == api_product["cggId"]:
                link = construct_link(product["link"]) if product["link"].startswith("/externalredirect") else product["link"]
                if not (is_link_functional(link) and is_link_functional(api_product["linkGeneralDesktop"])):
                    general_message.append("there is a problem with the link  '{}'  please check on the web site!".format(api_product["name"]))
    if general_message:
        fileUtils.send_email_to(mailTest, "important  some personal loan links may be down!!", general_message, [])
    return general_message



line = get_links_from_website()

# for el in line:
#     if el["link"].startswith("/externalredirect"):
#         print(el)
#         print(construct_link(el["link"]))



url2 ="https://www.topcompare.be/externalredirect?sendTo=aHR0cHM6Ly9sdDQ1Lm5ldC9jLz9zaT0xMzIxNSZsaT0xNTkwMDAxJndpPTMwMzExNiZ3cz0=&cggId=KBCX0001&product=Pr%C3%AAt%20personnel%20tous%20buts%20KBC&journeyId=01007747-c4dd-49a2-a89c-3ea493674bde"

u ="https://www.topcompare.be/externalredirect?sendTo"
# print(is_link_functional("https://www.topcompare.be/externalredirect?sendTo=aHR0cHM6Ly9sdDQ1L"))
# r = requests.request("GET",
#                      "https://www.topcompare.be/externalredirect?sendTo=aHR0cHM6Ly9sdDQ1Lm5ldC9jLz9zaT0xMzIxNSZsaT0xNTkwMDAxJndpPTMwMzExNiZ3cz0=&cggId=KBCX0001&product=Pr%C3%AAt%20personnel%20tous%20buts%20KBC&journeyId=01007747-c4dd-49a2-a89c-3ea493674bde",
#                      allow_redirects=True)
# r2 = requests.request("GET","https://www.topcompare.be/externalredirect",
#                      allow_redirects=True)
# print(r.status_code)
# print(r.text)
#
# # print(r2.status_code)
# # print(r2.text)
#
# print(r.url)
# print(r.history)
# print()
# print(r.headers)


# print(api_links())


# print(is_link_functional("https://loans.dhbbank.com/BelgiumLoanAppForm/Home/Index/FR/TCFR15?dclid=CjkKEQjwldHsBRDj6PL55KXsqfcBEiQA050No43HU0IMpzawvoWM3ZyUYNvCSDAnclGQD5QdficalpPw_wcB"))

# r = requests.get(url2)
# print(r.status_code)
# print(r.url)
# print(r.history)
# print(r.elapsed.total_seconds())


