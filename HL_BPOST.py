from bs4 import BeautifulSoup
import requests
import ast
import DataUtils

'''
        the rates are located in a script within the htmp document
'''
tab_col = [
    "PROVIDER",
    "PRODUCT TYPE",
    "LOAN FROM",
    "TO",
    "TAUX ANNUEL FIXE",
    "TAUX ANNUEL VARIABLE 5/5/5 CAP 5/5",
    "TAUX ANNUEL VARIABLE 10/5/5 CAP 5/5",
    "TAUX ANNUEL VARIABLE 10/5/5 CAP 2/2"
]

#retrives the rates as list fron script
def requestForRates():
    url = "https://www.bpostbanque.be/bpb/emprunter/credit-hypothecaire"
    response = requests.request("GET", url)

    #get the HTML document
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        #extract the script with text/backbase-xml as type
        rate_script = soup.find_all('script', attrs={"type" : "text/backbase-xml"})[0].text

        #convert the script to xml document
        soup_rate = BeautifulSoup(rate_script, "lxml")
        # print(soup_rate.prettify())
        # print(ast.literal_eval(soup_rate.find_all("property", attrs={"label": "Taux annuel fixe"})[0].value.text)[-1])
        # print(ast.literal_eval(soup_rate.find_all("property", attrs={"label": "Taux annuel fixe"})[0].value.text))

        #return the appropriate rate according to attribute as list [taux_annuel_fixe, taux_variable_1, taux_variable_2, taux_variable_3]
        return [
            ast.literal_eval(soup_rate.find_all("property", attrs={"label": "Taux annuel fixe"})[0].value.text)[-1],
            ast.literal_eval(
                soup_rate.find_all("property", attrs={"label": "Taux annuel variable 5/5/5"})[0].value.text),
            ast.literal_eval(
                soup_rate.find_all("property", attrs={"label": "Taux annuel variable 10/5/5 1"})[0].value.text),
            ast.literal_eval(
                soup_rate.find_all("property", attrs={"label": "Taux annuel variable 10/5/5 2"})[0].value.text)

        ]
    except:
        return None

#retrieves the min max amount from xml
def min_max_LoanAmount():
    url = "https://www.bpostbanque.be/bpb/emprunter/credit-hypothecaire"
    response = requests.request("GET", url)
    try :
        #get the HTML document
        soup = BeautifulSoup(response.text, 'html.parser')

        #extract the script with text/backbase-xml as type
        rate_script = soup.find_all('script', attrs={"type" : "text/backbase-xml"})[0].text

        #convert the script to xml document
        soup_rate = BeautifulSoup(rate_script, "lxml")

        #get the attribute Montant min Creditfrom and Montant max Credit the XML doc
        return ast.literal_eval(soup_rate.find_all("property", attrs={"label": "Montant min Credit"})[0].value.text), \
               ast.literal_eval(soup_rate.find_all("property", attrs={"label": "Montant max Credit"})[0].value.text)
    except:
        return None

#returns a data matrix
def formatData():
    return [["BPOST", "HOME LOAN", min_max_LoanAmount()[0], min_max_LoanAmount()[1]] + requestForRates()] if min_max_LoanAmount() and requestForRates() else None


def scraper():
    datamatrix = formatData()
    if datamatrix:
        return DataUtils.processData(datamatrix, tab_col, "BPOST HOME LOANS", "Bpost_hl_rates")
    else:
        print("LE LIEN BPOST HOME LOAN EST ACTUELLEMENT INDISPONIBLE")
        return None

# print(scraper())

# mail_list = ["bernaud.toukam@topcompare.be", "jihane.elkhyari@topcompare.be", "thomas.saclier@topcompare.be"]
# DataUtils.scrape_and_notify(scraper(), "BPOST HOMELOANS", mail_list)