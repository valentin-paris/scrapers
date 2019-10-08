from tabula import read_pdf
import DataUtils
# import fileUtils




#function used to convert pdf coordinates from mm to px
cpt = lambda d: d*(72/25.4)

positions = {
    "variable_rate": {
        "start": {
            "x": cpt(117),
            "y": cpt(110)

        },
        "end": {
            "x": cpt(132),
            "y": cpt(173)
        }
    },
}

#designed for variable rates data here we get the table at particular location in the pdf
def get_frame_by_coord(coordinates):
    try:
        return read_pdf("https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf", encoding='ISO-8859-1',
                        pages=1, silent= True, area=coordinates)
    except:
        print("THE LINK BNPPF FOR HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
        return None

def fix_rate_frame():
    try:
        return read_pdf("https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf"
                    , pages="2", silent= True).values.tolist()

    except:
        print("THE LINK BNPPF FOR HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
        return None

#can't extract the loan types from pdf hence the types are computed manually
#should be updated upon loan update
corres_name_variable_rates = {
    "variable": {
        0: {
            "title": "1/1 +3/-3",
            "term": "(durée < 10)"
        },
        1: {
            "title": "1/1 +3/-3",
            "term":  "Indice A (durée > 10 et ≤ 15 ans)"
        },
        2: {
            "title": "1/1 +3/-3",
            "term": "Indice A (durée > 15 et ≤ 20 ans)"
        },
        3:{
            "title":  "1/1 +3/-3",
            "term":  "Indice A (durée > 20 et ≤ 25 ans)"
        },
        4: {
            "title": "1/1 +3/-3", "term":
                "Indice A (durée > 25 et ≤ 30 ans)"
        },
        5: {
            "title": "1/1 +3/-3",
            "term": "Indice A mesualité constante (durée initiale 15 ans)"
        },
        6: {
            "title": "1/1 +3/-3",
            "term": "Indice A mesualité constante (durée initiale 20 ans)"
        },
        7: {
            "title": "1/1 +3/-3",
            "term": "Indice A mesualité constante (durée initiale 25 ans)"
        },
        8: {
            "title": "5/5 +4/-4",
            "term": "indice E"
        },
        9: {
            "title": "10/5 +2/-5",
            "term": "indice E"
        },
        10: {
            "title":"15/5 +2/-5",
            "term": "indice E(durée ≤ 25 ans)"
        }
    }
}

def bank_data():
    bank_data = []
    fix_rate_data = fix_rate_frame()
    for coord in positions:
        var_rate = get_frame_by_coord([
            positions[coord]["start"]["y"],
            positions[coord]["start"]["x"],
            positions[coord]["end"]["y"],
            positions[coord]["end"]["x"]
        ]).values.tolist()
        if len(var_rate) != len(corres_name_variable_rates["variable"]):
            if len(var_rate) > len(corres_name_variable_rates["variable"]):
                for i in range(len(var_rate)):
                    if i >= len(corres_name_variable_rates):
                        corres_name_variable_rates[i] = ""
            else:
                for i in range(len(corres_name_variable_rates["variable"])):
                    if i > len(var_rate):
                        corres_name_variable_rates.pop(i, None)
        else:
            for i in range(len(var_rate)):
                bank_data.append(["BNPPF",
                                  "HOME LOAN",
                                  corres_name_variable_rates["variable"][i]["title"],
                                  corres_name_variable_rates["variable"][i]["term"],
                                  var_rate[i][0]])

    for i in range(len(fix_rate_data[2:])):
        bank_data.append(["BNPPF", "HOME LOAN", "FIX RATE", fix_rate_data[i+2][0], fix_rate_data[i+2][3]])
    return bank_data

def scraper():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    return DataUtils.home_loan_scraper("BNPPF", bank_data())

# scraper()


