import tabula
import DataUtils
import ast



try:
    data_as_frameList = tabula.read_pdf("https://www.argenta.be/content/dam/argenta/documents/emprunter/credit-logement/Feuille%20de%20tarifs%20Cr%C3%A9dits%20hypoth%C3%A9caires.pdf", pages=3, multiple_tables=True )
except:
    data_as_frameList = None


def fixed_rate_procedure():
    tab_col = ["PROVIDER", "CREDIT TYPE", "CATEGORY", "TERM", "RATE"]
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
    else:
        print("THE ARGENTA HOME LOAN LINK IS MOMENTALLY UNAVAILABLE PLEASE CHECK ON THE WEBSITE!")
        return None



# print(fixed_rate_procedure())



for i in range(len(data_as_frameList)):
    print("position ", i)
    print(data_as_frameList[i])
    print(data_as_frameList[i].values.tolist())
    print()