import tabula
import DataUtils
import ast

try:
    data_as_frameList = tabula.read_pdf(
        "https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR",
        pages="all", multiple_tables=True)
except:
    data_as_frameList = None


# transform rate as string to rate as float from e.g  from 1,96 % to 1.96
def computeRateFrom(rate_string):
    return ast.literal_eval(rate_string.split(" ")[0].replace(",", "."))


# convert rate to string eg from 1.96 to 1,96 %
def convertRate_to_String(rate):
    return "{} %".format(str(rate).replace(".", ","))


# make the arithmetic addition of 2 strings and returns the result as string
def computeBase_rate(revue_rate, reduction):
    return convertRate_to_String(computeRateFrom(revue_rate) + computeRateFrom(reduction))


# extract the adjustment rates for base rates calculation
def getMinoredValues():
    return data_as_frameList[6].values.tolist()[4][1:]


# compute the scrape for the fixed rate home loan
def fix_rate_procedure():
    tab_col = ["PROVIDER", "CREDIT TYPE", "CATEGORY", "MIN TERM", "MAX TERM", "MONTH RATE", "ANNUAL RATE"]
    reduced_values = getMinoredValues()
    if data_as_frameList:
        try:
            dataMatrix = data_as_frameList[2].values.tolist()[2:]
            for i in range(len(dataMatrix)):
                dataMatrix[i][3:] = [
                    computeBase_rate(dataMatrix[i][3], reduced_values[0]),
                    computeBase_rate(dataMatrix[i][4], reduced_values[1])
                ]
                dataMatrix[i] = ["BELFIUS", "HOME LOAN FIXED RATES"] + dataMatrix[i]
            return DataUtils.processData(dataMatrix, tab_col, "BELFIUS HOME LOANS", "Belfius_hl_fixed_rates")
        except:
            print("THE STURCTURE OF BELFIUS THE PDF HAS BEEN MODIFIED PLEASE PROCESS IT BACK!")
            return None
    else:
        print("THE BELFIUS HOME LOAN LINK IS MOMENTALLY UNAVAILABLE PLEASE CHECK ON THE WEBSITE!")
        return None


# compute the scrape for variable rates
def variable_rate_procedure():
    tab_col = [
        "PROVIDER",
        "CREDIT TYPE",
        "CATEGORY",
        "MAX INCR OF CAP RATE \n MONTH RATE ",
        "MAX INCR OF CAP RATE \n ANNUAL RATE ",
        "MIN TERM",
        "MAX TERM",
        "BASE MONTH RATE",
        "BASE ANNUAL RATE"
    ]
    reduced_values = getMinoredValues()
    if data_as_frameList:
        try:
            dataMatrix = data_as_frameList[4].values.tolist()[2:] + data_as_frameList[5].values.tolist()
        except:
            print("THE STURCTURE OF THE PDF HAS BEEN MODIFIED PLEASE PROCESS IT BACK!")
            dataMatrix = None
        if dataMatrix:
            for i in range(len(dataMatrix)):
                dataMatrix[i][5:] = [
                    computeBase_rate(dataMatrix[i][5], reduced_values[0]),
                    computeBase_rate(dataMatrix[i][6], reduced_values[1])
                ]
                dataMatrix[i] = ["BELFIUS", "HOME LOAN VARIABLE RATES"] + dataMatrix[i]
            return DataUtils.processData(dataMatrix, tab_col, "BELFIUS HOME LOANS", "Belfius_hl_variable_rates")
        else:
            print("THE BELFIUS HOME LOAN LINK IS MOMENTALLY UNAVAILABLE PLEASE CHECK ON THE WEBSITE!")
            return None


def scraper():
    print("BELFIUS HOME LOAN PROCESSING...")
    return fix_rate_procedure() + variable_rate_procedure()

# scraper()
