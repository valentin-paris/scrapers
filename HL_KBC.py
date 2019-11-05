from tabula import read_pdf
# import fileUtils
import DataUtils
from DataUtils import cpt
from DataUtils import compute_coord_from_object

positions = {
    "fix_rate": {
        "start": {
            "x": cpt(192.44),
            "y": cpt(43)

        },
        "end": {
            "x": cpt(238.15),
            "y": cpt(62.12)
        }
    },

    "variable_rate (1/1/1)": {
        "start": {
            "x": cpt(6.27),
            "y": cpt(54.17)

        },
        "end": {
            "x": cpt(65.92),
            "y": cpt(65.10)
        }
    },
    "variable_rate (3/3/3)": {
        "start": {
            "x": cpt(71.69),
            "y": cpt(52.28)

        },
        "end": {
            "x": cpt(105.01),
            "y": cpt(65.34)
        }
    },
    "variable_rate (5/5/5)": dict(start=dict(x=cpt(132.46), y=cpt(52.23)), end= dict(x=cpt(167.90), y=cpt(65.13))),
}

def get_frame_by_coord(coordinates):
    try:
        return read_pdf("https://multimediafiles.kbcgroup.eu/ng/published/KBC/PDF/WONEN/kbc-woningkrediet-tarievenkaart.pdf", encoding='ISO-8859-1',
                        pages="1",  area=coordinates)
    except:
        print("THE LINK KBC FOR HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
        return None

def bankData():
    bankData = []
    for l_type in positions:
        product_list = get_frame_by_coord(compute_coord_from_object(positions, l_type)).values.tolist()
        for line in product_list:
            bankData.append(["KBC", "HOME LOAN", l_type, line[0], line[1]])
    return bankData

def scraper():
    return DataUtils.home_loan_scraper("KBC", bankData())


# scraper()

# mail_list = ["bernaud.toukam@topcompare.be", "jihane.elkhyari@topcompare.be", "thomas.saclier@topcompare.be", "quentin@topcompare.be"]
# mail_test = ["bernaud.toukam@topcompare.be"]
# DataUtils.scrape_and_notify(scraper(), "KBC HOMELOANS", mail_list)

