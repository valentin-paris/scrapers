import requests
from bs4 import BeautifulSoup
import json
import fileUtils


app_list =["AXA BANK", "ARGENTA", "BELFIUS", "CBC", "BNPPF", "BPOST", "CRELAN", "EUROPA BANK", "HELLO BANK",
            "ING", "KBC", "KEY TRADE", "BDK", "DEUTSCHE BANK", "FINTRO", "NAGELMACKERS", "VDK", "CPH", "BEOBANK"]
# urls and details for all androïd apps
android_bank_apps = {
    "AXA BANK": {"id": "be.axa.mobilebanking"},
    "ARGENTA": {"id": "be.argenta.bankieren"},
    "BELFIUS": {"id": "be.belfius.directmobile.android"},
    "CBC": {"id": "com.kbc.mobile.android.phone.cbc"},
    "BNPPF": {"id": "com.bnpp.easybanking"},
    "BPOST": {"id": "com.bpb.mobilebanking.smartphone.prd"},
    "CRELAN": {"id": "be.crelan.channels.mobile.android.store"},
    "EUROPA BANK": {"id": "com.mobile.europabank"},
    "HELLO BANK": {"id": "com.bnpp.hellobank"},
    "ING": {"id": "MyING.be"},
    "KBC": {"id": "com.kbc.mobile.android.phone.kbc"},
    "KEY TRADE": {"id": "be.keytradebank.phone"},
    "BDK": {"id": "be.bankdekremer.mobile"},
    "DEUTSCHE BANK": {"id": "com.db.pbc.mybankbelgium"},
    "FINTRO": {"id": "com.bnpp.easybanking.fintro"},
    "NAGELMACKERS": {"id": "be.dlbank.mobilebankingapp"},
    "VDK": {"id": "com.vdk.prod"},
    "CPH": {"id": "be.cph.cphmobile", "hl": "en"},
    "BEOBANK": {"id": "com.beobank_prod.bad", "hl": "en"}

}

def truncate(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


# extracts the rates and the reviews for a given bank in the android_bank_apps
def get_android_data(bank):
    url = "https://play.google.com/store/apps/details"
    headers = {
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "4f005cb9-3a23-4061-b606-c745ebc28d14,00d8d48b-ae93-44d4-b579-a9c8315840d0",
        'Host': "play.google.com",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "NID=193=BEOlb1_8iAn6lY1sHiOvduyvQdIQq8kFttG-CaBsKdF8ZWU_gZL3SAp2qNGp4MKR_Rlm5NUaAPh_1gIyJWZOf3pVRgPVq_IAssIcA9sdGrnNNEHLpnVXB2_bU-EcTQdJPdheC3bm0G0lb2QjgkMecdLKcfroZKnaVAbzJ2L0dks",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=android_bank_apps[bank])

    # store the DOM element in a soup
    soup = BeautifulSoup(response.text, "html.parser")

    # get the script of type application/ld+json containing  the data
    data = json.loads(soup.find('script', type='application/ld+json').text)

    # return the android data dict for a bank
    return {"app": "{} ANDROID".format(bank),
            "rate": truncate(float(data["aggregateRating"]["ratingValue"])),
            "reviews": int(data["aggregateRating"]["ratingCount"])
            }


# urls and details for all IOS apps
ios_bank_apps = {
    "CBC": {"id": "458081756"},
    "BELFIUS": {"id": "572835707"},
    "ARGENTA": {"id": "893585833"},
    "AXA BANK": {"id": "602565257"},
    "BNPPF": {"id": "516502006"},
    "BPOST": {"id": "1278930217"},
    "CRELAN": {"id": "893189359"},
    "HELLO BANK": {"id": "642897716"},
    "ING": {"id": "437203741"},
    "KBC": {"id": "458066754"},
    "KEY TRADE": {"id": "640974593"},
    "BDK": {"id": "1382705162"},
    "DEUTSCHE BANK": {"id": "1082668633"},
    "FINTRO": {"id": "544288649"},
    "NAGELMACKERS": {"id": "885804394"},
    "VDK": {"id": "895434057"},
    "CPH": {"id": "935210539"},
    "BEOBANK": {"id": "1008666594"}
}


# extracts the rates and the reviews for a given bank in the IOS_bank_apps
def get_ios_data(bank):
    # builds the appropriate URL using bank id from apps dict
    url = "https://amp-api.apps.apple.com/v1/catalog/BE/apps/{}".format(ios_bank_apps[bank]["id"])
    querystring = {"platform": "web",
                   "extend": "description%2CdeveloperInfo%2CeditorialVideo%2Ceula%2CfileSizeByDevice%2Cmessages"
                             "Screenshots%2CprivacyPolicyUrl%2CprivacyPolicyText%2CpromotionalText%2Cscreenshots"
                             "ByType%2CsupportURLForLanguage%2CversionHistory%2CvideoPreviewsByType%2CwebsiteUrl",
                   "include": "genres%2Cdeveloper%2Creviews%2Cmerchandised-in-apps%2Ccustomers-also-bought-apps%2"
                              "Cdeveloper-other-apps%2Capp-bundles%2Ctop-in-apps%2Ceula",
                   "l": "en-gb"}

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldlYlBsYXlLaWQifQ.eyJpc3MiOiJBTVBXZWJQb"
                         "GF5IiwiaWF0IjoxNTc0MTk3NDA3LCJleHAiOjE1ODk3NDk0MDd9.ael_GP97O4fyXJuQAQlmC7ieY-t-OOGFwtXShhVA"
                         "6m_p9Sq03D-_FiUKSfZ2iXGob3vPFnDe0s_OKI3Tg7KVaA",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Origin': "https://apps.apple.com",
        'Referer': "https://apps.apple.com/be/app/cbc-mobile/id458081756",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/78.0.3904.108 Mobile Safari/537.36",
        'Cache-Control': "no-cache",
        'Postman-Token': "ccc7059d-2c3f-4091-928e-cdd99976cf64,41a5415b-0e99-49bd-a486-66c28b11dc79",
        'Host': "amp-api.apps.apple.com",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "geo=BE",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    # return the IOS data dict for a bank
    return {
        "app": "{} IOS".format(bank),
        "rate": data["data"][0]["attributes"]["userRating"]["value"],
        "reviews": data["data"][0]["attributes"]["userRating"]["ratingCount"]
    }



# the rate_computer computes a weighted rate for apps
# parameters are data dict with rate and reviews keys
def rate_computer(android_data, ios_data):
    total_reviews = android_data["reviews"] + ios_data["reviews"]
    return truncate((android_data["rate"] * android_data["reviews"] + ios_data["rate"] * ios_data["reviews"])
                    / total_reviews)


def get_tc_rate():
    url = "https://www.topcompare.be/fr/compte-courant/api/products"

    headers = {
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "1fb23ed3-5d76-46f7-9f19-728d1a53fa78,7b298df6-081a-4a99-8209-4135e39954ee",
        'Host': "www.topcompare.be",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "analytics_id=8945f211-a382-4c70-90c9-7c674c4963bb; JSESSIONID=33F5410109808647BB90BD0AB821BF0E",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    app_rates = {}
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # get all the divs describing the products
    rate_tags = soup.find_all("div", {"class": "card-container row normal"})

    # extract the score tag and the score value
    for tag in rate_tags:
        score_tag = tag.find("div", {"data-col-title": "ScoreMobileApp"})
        app_rates[tag.attrs['data-cgg-id']] = float(
            score_tag.find("div", {"class": "column-primary card-column__value"}) \
            .text.strip().replace(",", "."))

    # return the rate of the apps in a dictionnary
    return app_rates

# return the bank for a product type
def product_to_bank(product):
    for key in android_bank_apps:
        if product[:3] in key:
            return key

# compare the ratings and build a message
def compare_rate_and_notify(delta):
    message = []

    # TC website rates and products
    tc_product_and_rates = get_tc_rate()
    for pdt in tc_product_and_rates:

        # correspond a product to the appropriate bank
        bank = product_to_bank(pdt)

        # compute the weighted rate if the bank has both apps
        if bank in android_bank_apps:
            if bank in ios_bank_apps:
                actual_rate = rate_computer(get_android_data(bank), get_ios_data(bank))
            else:
                # else consider the unique rate
                actual_rate = get_android_data(bank)["rate"]

        elif bank in ios_bank_apps:
            actual_rate = get_ios_data(bank)["rate"]
        else:
            # if the bank is not present in any of the app repository
            actual_rate = None

        # if the difference btn the actual rate and the tc_web site rate gt delta
        if actual_rate and abs(actual_rate - tc_product_and_rates[pdt]) > delta:
            message += ["{} .... NOT OK!".format(bank)]
    if not message:
        message += ["all the app ratings are up to date"]
    return message

# print(compare_rate_and_notify(0.5))


def app_rate_frame():
    header = ["APP", "ANDROID_RATE", "ANDROID_REVIEWS", "IOS_RATE", "IOS_REVIEWS", "WEIGHTED_RATE"]
    frame = []
    for bank_app in app_list:
        if bank_app in ios_bank_apps:
            if bank_app in android_bank_apps:
                and_data = get_android_data(bank_app)
                ios_data = get_ios_data(bank_app)
                frame.append([bank_app, and_data["rate"], and_data["reviews"], ios_data["rate"], ios_data["reviews"],
                              rate_computer(and_data, ios_data)])
            else:
                frame.append([bank_app, "-", "-", get_ios_data(bank_app)["reviews"], get_ios_data(bank_app)["rate"],
                              get_ios_data(bank_app)["rate"]])
        else:
                frame.append([bank_app, get_android_data(bank_app)["rate"], get_android_data(bank_app)["reviews"],
                              "-", "-", get_android_data(bank_app)["rate"]])
    fileUtils.displayRates(header, frame)
    return frame


print(app_rate_frame())






