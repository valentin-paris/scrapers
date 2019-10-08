import requests
from bs4 import BeautifulSoup
from fileUtils import no_double
import json


#returns all active personnal loans from the web-site
def personal_loan_links():
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

#returns links for particular car age and type
def links_by_car_age(car_age, car_type):
    link_list = []
    url = "https://www.topcompare.be/api/personal-loan/v2/products"

    querystring = {
                    "journeyId": "207089e3-f8ed-442d-9ff5-f5397df81fa6",
                    "category": "vehicleLoan",
                    "wantToBorrow": "15000",
                    "wantToBorrowTime": "48",
                    "wantToBorrowTimeUnit": "personal-loan.filter.vehicleLoan.default.wantToBorrowTimeUnitKey",
                    "greenOrClassicCar": car_type,
                    "carAge": car_age}

    headers = {
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "e947b905-571c-477e-b314-252de2ff980e,5aa72bb4-6916-4af3-9aaf-b47942957b08",
        'Host': "www.topcompare.be",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "analytics_id=8945f211-a382-4c70-90c9-7c674c4963bb; JSESSIONID=33F5410109808647BB90BD0AB821BF0E; AWSELB=5907FD4314C525EB17E3302227917862180282663C9253C7E2E142C38D3AD8A65ECC310A62E932FAB0B397F83780C3268F4A83D7017DAF7861D5E3A2ABA4A2470B514F010B",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    soup = BeautifulSoup(response.text, "html.parser")

    btn_list = soup.find_all("button")

    for i in range(len(btn_list)):
        if "data-url" in btn_list[i].attrs:
            link_list.append({"id": btn_list[i].attrs["data-cgg-id"], "link": btn_list[i].attrs["data-url"]})
    return no_double(link_list)

#compute links for all the types of car
def car_loan_links():
    ages_of_car = ("new", "0-1", "2-3", "3-4", "4-5", "5+")
    types_of_car = ("classic", "green")
    all_car_links = []
    for car_type in types_of_car:
        for car_age in ages_of_car:
            all_car_links += links_by_car_age(car_age, car_type)
    return no_double(all_car_links)

#returns links for particular moto age
def moto_links_by_age(moto_age):
    link_list = []
    url = "https://www.topcompare.be/api/personal-loan/v2/products"

    querystring = {"journeyId": "74ec2d64-7758-4a05-bf53-28de1dc24bc1", "category": "moto", "wantToBorrow": "15000",
                   "wantToBorrowTime": "48",
                   "wantToBorrowTimeUnit": "personal-loan.filter.moto.default.wantToBorrowTimeUnitKey", "carAge": moto_age}

    headers = {
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "394b050d-aacd-48ee-bbb7-db67fa8c6918,a6911efd-b2bc-424a-86df-08d5140a6998",
        'Host': "www.topcompare.be",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "analytics_id=8945f211-a382-4c70-90c9-7c674c4963bb; JSESSIONID=33F5410109808647BB90BD0AB821BF0E; AWSELB=5907FD4314C525EB17E3302227917862180282663C9253C7E2E142C38D3AD8A65ECC310A62E7F6249152172C68019D848119A655497DAF7861D5E3A2ABA4A2470B514F010B",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    soup = BeautifulSoup(response.text, "html.parser")

    btn_list = soup.find_all("button")

    for i in range(len(btn_list)):
        if "data-url" in btn_list[i].attrs:
            link_list.append({"id": btn_list[i].attrs["data-cgg-id"], "link": btn_list[i].attrs["data-url"]})
    return no_double(link_list)

#compute links for all the types of moto
def all_moto_links():
    ages_of_moto = ("new", "0-1", "2-3", "3-4", "4-5", "5+")
    all_links = []
    for age in ages_of_moto:
        all_links += moto_links_by_age(age)
    return no_double(all_links)

#returns the links for all the products without duplicates
def all_loan_links():
   return no_double(personal_loan_links() + car_loan_links() + all_moto_links())

#contruct a link by adding appropriate head to the web-link
def construct_link(web_link):
    return "https://www.topcompare.be{}".format(web_link)

#returns true if a link has a 200 status code else false
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

def car_links_from_api():
    url = "https://www.topcompare.be/api/personal-loan/v2/loans/vehicleLoan"

    querystring = {"backendRendering": "false", "journeyId": "ea2aca0a-33ff-402d-9908-326c72969241",
                   "sortBy": ["mrp%2B", "apr%2B", "trp%2B"], "wantToBorrow": "15000", "greenOrClassicCar": "classic",
                   "wantToBorrowTime": "48", "wantToBorrowTimeUnit": "month", "carAge": "new", "lang": "fr",
                   "pageSize": "15"}

    response = requests.request("GET", url, params=querystring)

    return (json.loads(response.text)["products"])

def pers_links_from_api():
    url = "https://www.topcompare.be/api/personal-loan/v2/loans/personalLoan"

    querystring = {"backendRendering": "false", "journeyId": "3248cdbf-ad5f-443f-ae47-6d021c623f64",
                   "sortBy": ["mrp%2B", "apr%2B", "trp%2B"], "wantToBorrow": "9233", "wantToBorrowTime": "36",
                   "wantToBorrowTimeUnit": "month", "lang": "fr", "pageSize": "15"}
    response = requests.request("GET", url, params=querystring)

    return (json.loads(response.text)["products"])

#returns links for moto from api
def moto_links_from_api():
    url = "https://www.topcompare.be/api/personal-loan/v2/loans/moto"

    querystring = {"backendRendering": "false", "journeyId": "ea2aca0a-33ff-402d-9908-326c72969241",
                   "sortBy": ["mrp%2B", "apr%2B", "trp%2B"], "wantToBorrow": "15000", "wantToBorrowTime": "48",
                   "wantToBorrowTimeUnit": "month", "carAge": "new", "lang": "fr", "pageSize": "15"}

    response = requests.request("GET", url, params=querystring)

    return (json.loads(response.text)["products"])

#compute all the links from the different api
def api_links():
    return pers_links_from_api() + car_links_from_api() + moto_links_from_api()

#check if all links and corresponding api links both return a 200 status code
#and build the message to be delivered
def check_links():
    print("checking links ...")
    general_message = []
    for product in all_loan_links():
        for api_product in api_links():
            if product["id"] == api_product["cggId"]:
                link = construct_link(product["link"]) if product["link"].startswith("/externalredirect") else product["link"]
                if not (is_link_functional(link) and is_link_functional(api_product["linkGeneralDesktop"])):
                    print("there is a problem with the link  '{}'  please check on the web site!".format(api_product["name"]))
                    general_message.append("there is a problem with the link  '{}'  please check on the web site!".format(api_product["name"]))
    if not general_message:
        general_message += ["all the loan links are functional".upper()]
    return general_message









