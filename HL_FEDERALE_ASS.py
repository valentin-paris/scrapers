from tabula import read_pdf
import DataUtils
from DataUtils import home_loan_scraper
# import fileUtils

try:
    data_as_frameList = read_pdf("https://www.federale.be/docs/default-source/default-document-library/particulieren-particuliers/tarif-ch-30-01-2019.pdf?sfvrsn=9f4b78d7_5",
                                        pages= "1", silent=True,  multiple_tables=True )
except:
    print("THE LINK FOR FEDERALE HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
    data_as_frameList = None


def bankData():
    all_loans = {
        1: "fix rate",
        2: "variable 15/5 +2-2",
        3: " variable 10/5 +2-2",
        4: "variable 5/5 +2-2",
        5: "variable 1/1 +3-3"
    }
    bankData = []
    if data_as_frameList:
        for i in range(len(data_as_frameList)):
            l_type = all_loans[i+1].upper()
            l_data = data_as_frameList[i].values.tolist()[3:]
            for line in l_data:
                bankData.append(["FEDERALE ASSUR", "HOME LOAN", l_type, line[0][1:], line[1]])
    return bankData


def scraper():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    return home_loan_scraper("FEDERALE", bankData())

# print(scraper())
# scraper()
#
# print(data_as_frameList)

