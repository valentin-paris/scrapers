from tabula import read_pdf
import DataUtils
# import fileUtils


cpt = lambda d: d*(72/25.4)

positions = {
    "fix_rate": {
        "start": {
            "x": cpt(353),
            "y": cpt(92.5)

        },
        "end": {
            "x": cpt(455),
            "y": cpt(130)
        }
    },

    "variable_rate (1/1/1)": {
        "start": {
            "x": cpt(29),
            "y": cpt(92.5)

        },
        "end": {
            "x": cpt(140.5),
            "y": cpt(130)
        }
    },
    "variable_rate (3/3/3)": {
        "start": {
            "x": cpt(145),
            "y": cpt(92.5)

        },
        "end": {
            "x": cpt(245.5),
            "y": cpt(130)
        }
    },
    "variable_rate (5/5/5)": dict(start=dict(x=cpt(250), y=cpt(92.5)), end= dict(x=cpt(348.5), y=cpt(130))),
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
        return read_pdf("https://www.cbc.be/content/dam/particulieren/f-cbc/product/lenen/Wonen/woonkrediet/Carte%20des%20taux%20des%20Cr%C3%A9dits%20logement.pdf", encoding='ISO-8859-1',
                        pages="1",  area=coordinates)
    except:
        print("THE LINK CBC FOR HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
        return None

def bank_data():
    bank_data = []
    try :
        for loan_type in positions:
            if loan_type == "fix_rate":
                loan_data = get_frame_by_coord(compute_coord_from_object(loan_type)).values.tolist()[1:]
                for i in range(len(loan_data)):
                    bank_data.append(["CBC", "HOME LOAN", loan_type.upper(), loan_data[i][0], "{} %".format(loan_data[i][1])])
            elif loan_type == "variable_rate (1/1/1)":
                loan_data = get_frame_by_coord(compute_coord_from_object(loan_type)).values.tolist()[3:]
                for i in range(len(loan_data)):
                    bank_data.append(["CBC", "HOME LOAN", loan_type.upper(), loan_data[i][0], loan_data[i][1]])
            else:
                loan_data = get_frame_by_coord(compute_coord_from_object(loan_type)).values.tolist()[3:]
                for i in range(len(loan_data)):
                    bank_data.append(["CBC",
                                      "HOME LOAN",
                                      loan_type.upper(),
                                      "{} ans".format(loan_data[i][0].split("ans")[0]),
                                      "{}%".format(loan_data[i][0].split("ans")[1].split("%")[0])
                                      ])
    except:
        print("THE STRUCTURE OF THE CBC HOME LOAN PDF HAS BEEN MODIFIED PLEASE PROCESS IT BACK")

    return bank_data

def scraper():
    print("CBC HOME LOAN PROCESSING ...")
    tab_col = ["PROVIDER", "CATEGORY", "CREDIT TYPE", "TERM", "RATE"]
    data_matrix = bank_data()
    if data_matrix:
        # fileUtils.displayRates(tab_col, data_matrix)
        return DataUtils.processData(data_matrix, tab_col, "BVBR HOME LOANS", "bvbr_hl_rates")

# scraper()