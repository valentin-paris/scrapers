import tabula
from tabula import read_pdf
import DataUtils
# import fileUtils

try:
    data_as_frameList = tabula.read_pdf("https://www.ing.be/static/legacy/SiteCollectionDocuments/Bareme_CH_FR.pdf",
                                        pages= "1", silent=True,  multiple_tables=True )
except:
    print("THE LINK FOR ING HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
    data_as_frameList = None


# print(data_as_frameList)

cpt = lambda d: d*(72/25.4)

positions = {
    "variable_rate": {
        "start": {
            "x": cpt(8),
            "y": cpt(62)

        },
        "end": {
            "x": cpt(81.31),
            "y": cpt(160.20)
        }
    },
}

def compute_coord_from_object(object):
    return [
                positions[object]["start"]["y"],
                positions[object]["start"]["x"],
                positions[object]["end"]["y"],
                positions[object]["end"]["x"]
            ]


def get_frame_by_coord(coordinates):
    try:
        return read_pdf("https://www.ing.be/static/legacy/SiteCollectionDocuments/Bareme_CH_FR.pdf", encoding='ISO-8859-1',
                        pages="1",  area=coordinates)
    except:
        print("THE LINK CBC FOR HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
        return None

def bank_data():
    bank_data = []
    content = get_frame_by_coord(compute_coord_from_object("variable_rate")).values.tolist()
    if content:
        for line in content[:6]:
            bank_data.append(["ING", "HOME LOAN", "FIX RATE", line[0], line[2]])
        for i in range(len(content[8:14])):
            bank_data.append(["ING", "HOME LOAN", content[7][0], content[i + 8][0], content[i + 8][2]])
        for i in range(len(content[15:20])):
            bank_data.append(["ING", "HOME LOAN", content[14][0], content[i + 15][0], content[i + 15][2] ])
        for i in range(len(content[21:25])):
            bank_data.append(["ING", "HOME LOAN", content[20][0], content[i + 21][0], content[i + 15][2]])
        for i in range(len(content[26:])):
            bank_data.append(["ING", "HOME LOAN", content[25][0], content[i + 26][0], content[i + 26][2]])
    return bank_data


def scraper():
    print("ING HOME LOAN PROCESSING ...")
    tab_col = ["PROVIDER", "CATEGORY", "CREDIT TYPE", "TERM", "RATE"]
    data_matrix = bank_data()
    if data_matrix:
        # fileUtils.displayRates(tab_col, data_matrix)
        return DataUtils.processData(data_matrix, tab_col, "BVBR HOME LOANS", "bvbr_hl_rates")

# scraper()



