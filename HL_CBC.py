from tabula import read_pdf
import DataUtils
# import fileUtils


cpt = lambda d: d*(72/25.4)

positions = {
    "fix_rate": {
        "start": {
            "x": cpt(222.19),
            "y": cpt(58)

        },
        "end": {
            "x": cpt(265.63),
            "y": cpt(77.58)
        }
    },

    "variable_rate (1/1/1)": {
        "start": {
            "x": cpt(19.23),
            "y": cpt(63.74)

        },
        "end": {
            "x": cpt(86.27),
            "y": cpt(83.82)
        }
    },
    "variable_rate (3/3/3)": {
        "start": {
            "x": cpt(89.29),
            "y": cpt(67.55)

        },
        "end": {
            "x": cpt(150.15),
            "y": cpt(80.49)
        }
    },
    "variable_rate (5/5/5)": {
        "start": {
            "x": cpt(154.40),
            "y": cpt(67.38)

        },
        "end": {
            "x": cpt(216.79),
            "y": cpt(80.49)
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
    return DataUtils.home_loan_scraper("CBC", bank_data())

# scraper()

# mail_list = ["bernaud.toukam@topcompare.be", "jihane.elkhyari@topcompare.be", "thomas.saclier@topcompare.be"]
# DataUtils.scrape_and_notify(scraper(), "CBC HOMELOANS", mail_list)
