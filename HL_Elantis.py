import requests
import json

home_types = ("home", "flat")
category = ("ratefix", "rate1055", "rate555", "rate333")

amount_range = list(range(12500, 750000, 5000)) + [750000]
test_range = list(range(25000, 35000, 5000))
term_range = list(range(10, 26))

car = lambda l: l[0]
cdr = lambda l: l[1:]
def sort_by_category(all_pdt, category):
    if all_pdt == []:
        return []
    elif car(all_pdt)["name"] == category:
        return [car(all_pdt)] + sort_by_category(cdr(all_pdt), category)
    else:
        return sort_by_category(cdr(all_pdt), category)

def req_data_for_loan(l_type, amount, duration):
    url = "https://www.elantis.be/fr/simulateur-credit-hypothecaire/"

    querystring = {"amount": amount, "duration": duration, "mode": "total", "type": l_type}

    headers = {
        'x-doing-ajax': "true",
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "5a20513e-b8a6-4937-b76f-1dbc465175fd,c4a74205-bf4e-424d-98d8-2e91a3aac66e",
        'Host': "www.elantis.be",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "pll_language=fr",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return json.loads(response.text)


def bank_data():
    bank_data = []
    for h_type in home_types:
        data_for_htype = []
        for mnt in test_range:
            for term in term_range:
                print(term)
                loan_list = req_data_for_loan(h_type, mnt, term)
                for l in loan_list:
                    print(l)
                    print(".", end='')
                    l["h_type"] = h_type
                    data_for_htype.append(l)
            print()
        bank_data.append(data_for_htype)
    return bank_data

def bank_data_per_category(b_data):
    bank_data = []
    for data_set in b_data:
        data_category = []
        for cat in category:
            data_category.append(sort_by_category(data_set, cat))
        bank_data.append(data_category)
    return bank_data


# print(bank_data_per_category(bank_data()))
test = bank_data_per_category(bank_data())


for i in range(len(test)):
    for j in range(len(test[i])):
        for t in range(len(test[i][j])):
            print(test[i][j][t])

# print(req_data_for_loan("home", 25000, 22))

print(bank_data())