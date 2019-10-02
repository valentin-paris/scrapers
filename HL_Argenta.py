import tabula
import DataUtils


try:
    data_as_frameList = tabula.read_pdf("https://www.argenta.be/content/dam/argenta/documents/emprunter/credit-logement"
                                        "/Feuille%20de%20tarifs%20Cr%C3%A9dits%20hypoth%C3%A9caires.pdf",
                                        pages=3, multiple_tables=True, silent=True )
except:
    print("THE ARGENTA HOME LOAN LINK IS MOMENTALLY UNAVAILABLE PLEASE CHECK ON THE WEBSITE!")
    data_as_frameList = None



def fixed_rate_data():
    if data_as_frameList:
        try:
            data = data_as_frameList[8]
            fixed_rate_matrix = []
            for i in range(len(data.values.tolist())):
                fixed_rate_matrix.append(["ARGENTA", "HOME LOAN", "FIXED RATE", data.values.tolist()[i][1], data.values.tolist()[i][3]])
            return fixed_rate_matrix
        except:
            print("THE STURCTURE OF THE ARGENTA PDF HOME LOAN HAS BEEN MODIFIED PLEASE PROCESS IT BACK!")
            return None


#here we scrape a pdf and split the table data to extract valuable data
#we make use of the format method for a readable presentation
def variable_data():
    req_data = data_as_frameList[1:8]
    bank_data = []
    for i in range(len(req_data)):
        if i < 4:
            for j in range(len(req_data[i].values.tolist())):
                bank_data.append([
                    "ARGENTA",
                    "HOME LOAN",
                    req_data[i].values.tolist()[0][0],
                    req_data[i].values.tolist()[j][1],
                    req_data[i].values.tolist()[j][3]])
        elif i == 4:
            for j in range(len(req_data[i].values.tolist())):
                if j != 2:
                    bank_data.append([
                        "ARGENTA",
                        "HOME LOAN",
                        req_data[i].values.tolist()[0][0],
                        req_data[i].values.tolist()[j][1],
                        req_data[i].values.tolist()[j][3]])

        else:
            for j in range(len(req_data[i].values.tolist())):
                if j != 1:
                    bank_data.append([
                        "ARGENTA",
                        "HOME LOAN",
                        req_data[i].values.tolist()[0][0],
                        req_data[i].values.tolist()[j][1],
                        req_data[i].values.tolist()[j][3]])

    return bank_data


def scraper():
    DataUtils.home_loan_scraper("ARGENTA", fixed_rate_data()+variable_data())











