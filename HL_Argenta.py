import tabula
import DataUtils
import ast
# import fileUtils



try:
    data_as_frameList = tabula.read_pdf("https://www.argenta.be/content/dam/argenta/documents/emprunter/credit-logement/Feuille%20de%20tarifs%20Cr%C3%A9dits%20hypoth%C3%A9caires.pdf", pages=3, multiple_tables=True )
except:
    print("THE ARGENTA HOME LOAN LINK IS MOMENTALLY UNAVAILABLE PLEASE CHECK ON THE WEBSITE!")
    data_as_frameList = None


def fixed_rate_procedure():
    tab_col = ["PROVIDER", "CATEGORY", "CREDIT TYPE", "TERM", "RATE"]
    if data_as_frameList:
        try:
            data = data_as_frameList[8]
            fixed_rate_matrix = []
            for i in range(len(data.values.tolist())):
                if i != 3:
                    term = data.values.tolist()[i][1].split("ans")[0]
                    rate = data.values.tolist()[i][1].split("ans")[1]
                    fixed_rate_matrix .append(["ARGENTA", "HOME LOAN", "FIXED RATE", "{}ans".format(term), rate])
                else:
                    term_1 = data.values.tolist()[i][1].split("%")[0].split("ans")[0]
                    rate_1 = data.values.tolist()[i][1].split("%")[2].split("ans")[1]
                    term_2 = data.values.tolist()[i][1].split("%")[2].split("ans")[0]
                    rate_2 = data.values.tolist()[i][1].split("%")[3]
                    fixed_rate_matrix.append(["ARGENTA", "HOME LOAN", "FIXED RATE", "{}ans".format(term_1), "{}%".format(rate_1)])
                    fixed_rate_matrix.append(["ARGENTA", "HOME LOAN", "FIXED RATE", "{}ans".format(term_2), "{}%".format(rate_2)])
            return DataUtils.processData(fixed_rate_matrix, tab_col, "ARGENTA HOME LOANS", "argenta_hl_fixed_rates")
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
                loan_type = req_data[i].values.tolist()[0][0]
                if j != 1:
                    term = "{} ans".format(req_data[i].values.tolist()[j][1].split("ans")[0])
                    rate = req_data[i].values.tolist()[j][1].split("ans")[1]
                    bank_data.append(["ARGENTA", "HOME LOAN", loan_type, term, rate])
                else:
                    term1 = "{} ans".format(req_data[i].values.tolist()[j][1].split("ans")[0])
                    term2 = "<{} ans".format(req_data[i].values.tolist()[j][1].split("ans")[1].split("<")[1])
                    rate1 = "{}%".format(req_data[i].values.tolist()[j][1].split("ans")[2].split("%")[0])
                    rate2 = "{}%".format(req_data[i].values.tolist()[j][1].split("ans")[2].split("%")[1])
                    bank_data.append(["ARGENTA", "HOME LOAN", loan_type, term1, rate1])
                    bank_data.append(["ARGENTA", "HOME LOAN", loan_type, term2, rate2])
        else:
            loan_type = req_data[i].values.tolist()[0][0].split("<")[0]
            term1 = "<{}".format(req_data[i].values.tolist()[0][0].split("<")[1])
            rate1 = req_data[i].values.tolist()[0][2]
            bank_data.append(["ARGENTA", "HOME LOAN", loan_type, term1, rate1])
            term2 = "<{}".format(req_data[i].values.tolist()[1][0].split("<")[1])
            rate2 = req_data[i].values.tolist()[1][2]
            bank_data.append(["ARGENTA", "HOME LOAN", loan_type, term2, rate2])
    return bank_data

def variable_rate_procedure():
    if data_as_frameList:
        tab_col = ["PROVIDER", "CATEGORY", "CREDIT TYPE", "TERM", "RATE"]
        try:
            data_matrix = variable_data()
        except:
            print("THE SRUCTURE OF ARGENTA LOAN PDF HAS BEEN MODIFIED PLEASE PROCESS IT BACK")
            data_matrix = None
        if data_matrix:
            return DataUtils.processData(data_matrix, tab_col, "ARGENTA HOME LOANS", "argenta_hl_variable_rates")
            # fileUtils.displayRates(tab_col, data_matrix)

def scraper():
    return fixed_rate_procedure() + variable_rate_procedure()



