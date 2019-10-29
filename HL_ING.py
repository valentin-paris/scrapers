from tabula import read_pdf
import DataUtils



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
        print("THE LINK ING FOR HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
        return None

def bank_data():
    bank_data = []
    try:
        content = get_frame_by_coord(compute_coord_from_object("variable_rate")).values.tolist()
    except:
        content = None
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
    return DataUtils.home_loan_scraper("ING", bank_data())

scraper()







