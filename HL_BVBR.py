from tabula import read_pdf
import DataUtils
from DataUtils import home_loan_scraper
# import fileUtils

cpt = lambda d: d*(72/25.4)

#functional expressions to check for particular value in frame
car = lambda l: l[0]
cdr = lambda l: l[1:]
def check_for_val_in_frame(frame, value):
    if frame == []:
        return []
    elif value in car(car(frame)):
        return [car(frame)] + check_for_val_in_frame(cdr(frame), value)
    else:
        return check_for_val_in_frame(cdr(frame), value)

#define the various coordinates for each loan matrix
position = {
    "fix_rate": {
        "start": {
            "x": cpt(19.42),
            "y": cpt(55.77)

        },
        "end": {
            "x": cpt(93.21),
            "y": cpt(79.77)
        }
    },
    "variable_rate": {
        "start": {
            "x": cpt(19.42),
            "y": cpt(86.01)

        },
        "end": {
            "x": cpt(93.21),
            "y": cpt(168.21)
        }
    },

}

#here we get the tables according to their position on the pdf
def req_for_frame(coordinates):
    try:
        return read_pdf('https://www.banquevanbreda.be/media/2675/tariefregeling-jvb-fr-293.pdf', encoding='ISO-8859-1',
                       pages=1, area=coordinates, pandas_options={'header': None}, silent=True)
    except:
        print("THE BVBR LINK FOR HOME LOANS HAS BEEN MODIFIED PLEASE CHECK FOR THE NEW LINK ON THE WEBSITE! ")
        return None

def bank_data():
    bank_data = []
    for coord in position:
        rate_frame = req_for_frame([
            position[coord]["start"]["y"],
            position[coord]["start"]["x"],
            position[coord]["end"]["y"],
            position[coord]["end"]["x"]])
        if coord == "fix_rate":
            try:
                for line in rate_frame.values.tolist():
                    bank_data.append(["BVBR", "HOME LOAN", "FIX_RATE",  line[0].split("max.")[1],  line[1]])
            except:
                print("THE PDF STRUCTURE OF BVBR HOME LOANS HAS BEEN MODIFIED PLEASE PROCESS IT BACK!")
        else:
            variable_frame = check_for_val_in_frame(rate_frame.values.tolist(), "Variabilité")
            if variable_frame:
                for line in variable_frame:
                    bank_data.append(["BVBR", "HOME LOAN", line[0], line[1], line[2]])
            else:
                print("THE PDF STRUCTURE OF BVBR HOME LOANS HAS BEEN MODIFIED PLEASE PROCESS IT BACK!")
    return bank_data

def scraper():
    return home_loan_scraper("BVBR", bank_data())

# scraper()