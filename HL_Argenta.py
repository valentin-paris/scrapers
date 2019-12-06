import tabula
import DataUtils

mail_list = ["bernaud.toukam@topcompare.be", "jihane.elkhyari@topcompare.be", "thomas.saclier@topcompare.be"]
test_mail = ["bernaud.toukam@topcompare.be"]
try:
    data_as_frameList = tabula.read_pdf("https://www.argenta.be/content/dam/argenta/documents/emprunter/credit-logement"
                                        "/Feuille%20de%20tarifs%20Cr%C3%A9dits%20hypoth%C3%A9caires.pdf",
                                        pages=2, multiple_tables=True, silent=True )
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
            print("THE STURCTURE OF THE ARGENTA PDF HOME LOAN FOR FIXED RATE HAS BEEN MODIFIED PLEASE PROCESS IT BACK!")
            return None


#here we scrape a pdf and split the table data to extract valuable data
#we make use of the format method for a readable presentation
#the logic here should be adapted to structure of the PDF
def variable_data():
    try:
        #since the data starts from 1 the indices also are shifted of 1 ahead
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
                    if j != 1:
                        bank_data.append([
                            "ARGENTA",
                            "HOME LOAN",
                            req_data[i].values.tolist()[0][0],
                            "{} ans".format(req_data[i].values.tolist()[j][1].split("ans")[0]),
                            req_data[i].values.tolist()[j][1].split("ans")[1]
                        ])

            else:
                for j in range(len(req_data[i].values.tolist())):
                    bank_data.append([
                        "ARGENTA",
                        "HOME LOAN",
                        req_data[i].values.tolist()[0][0].split("<")[0],
                        "<{}".format(req_data[i].values.tolist()[j][0].split("<")[1]),
                        req_data[i].values.tolist()[j][2]
                    ])
        return bank_data
    except:
        print("THE STURCTURE OF THE ARGENTA PDF HOME LOAN FOR VARIABLE RATES HAS BEEN MODIFIED PLEASE PROCESS IT BACK!")
        return None


def scraper():
    return DataUtils.home_loan_scraper("ARGENTA", fixed_rate_data()+variable_data())

# DataUtils.scrape_and_notify(scraper(), "ARGENTA HOME LOANS", test_mail)




