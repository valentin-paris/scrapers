from tabula import read_pdf
# import fileUtils
import DataUtils
from DataUtils import cpt
from DataUtils import compute_coord_from_object

positions = {
    "fix_rate": {
        "start": {
            "x": cpt(295),
            "y": cpt(70)

        },
        "end": {
            "x": cpt(398),
            "y": cpt(105)
        }
    },

    "variable_rate (1/1/1)": {
        "start": {
            "x": cpt(9.4),
            "y": cpt(78)

        },
        "end": {
            "x": cpt(100.5),
            "y": cpt(105)
        }
    },
    "variable_rate (3/3/3)": {
        "start": {
            "x": cpt(109),
            "y": cpt(78)

        },
        "end": {
            "x": cpt(192),
            "y": cpt(105)
        }
    },
    "variable_rate (5/5/5)": dict(start=dict(x=cpt(203), y=cpt(78)), end= dict(x=cpt(288), y=cpt(105))),
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
        product_list = get_frame_by_coord(compute_coord_from_object( positions, l_type)).values.tolist()
        for line in product_list:
            bankData.append(["KBC", "HOME LOAN", l_type, line[0], line[1]])
    return bankData

def scraper():
    print("KBC HOME LOAN PROCESSING ...")
    tab_col = ["PROVIDER", "CATEGORY", "CREDIT TYPE", "TERM", "RATE"]
    data_matrix = bankData()
    if data_matrix:
        # fileUtils.displayRates(tab_col, data_matrix)
        return DataUtils.processData(data_matrix, tab_col, "BVBR HOME LOANS", "bvbr_hl_rates")


# scraper()