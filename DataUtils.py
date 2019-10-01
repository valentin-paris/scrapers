import fileUtils
from  tabula import read_pdf

#BankData is a matrix ie list of list of jsonData type amount duration and rate
def createGroups(bankData):
    loanGroups = {}
    for loanList in bankData:
        for loanElement in loanList:
            if (loanElement['type'], loanElement['duration'], loanElement['rate'], loanElement['productID']) not in\
                    loanGroups.keys():
                loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'], loanElement['productID']
                            )] = [loanElement['amount']]
            else:
                loanGroups[(loanElement['type'], loanElement['duration'], loanElement['rate'], loanElement['productID']
                            )].append(loanElement['amount'])
    return loanGroups


def formatDataFrom(groups, provider):
    frameToExport = []
    for eachGroup in groups:
        frameToExport.append([provider, eachGroup[3], eachGroup[0], min(map(int, groups[eachGroup])),
                              max(map(int, groups[eachGroup])), int(eachGroup[1]), float(eachGroup[2])])
    return frameToExport


def processData(dataMatrix, tab_Column, directoryName, fileName):
    fileUtils.displayRates(tab_Column, dataMatrix)
    return fileUtils.upToDate(fileName, directoryName, dataMatrix, tab_Column, [])


def addAtributes(loanList, lType, duration, rate, pdtID):
    for loan in loanList:
        loan['type'] = lType
        loan['duration'] = duration
        loan['rate'] = rate
        loan['productID'] = pdtID

#define a more generic function to process the data
def proc_data(b_data, provider, dir_name, file_name, tab_col):
    data_matrix = formatDataFrom(createGroups(b_data), provider)
    if data_matrix:
        fileUtils.displayRates(tab_col, data_matrix)
        return fileUtils.upToDate(file_name, dir_name, data_matrix, tab_col, [])
    else:
        return None


#to compute coordinate from mm to px
cpt = lambda d: d*(72/25.4)

#returns a data_frame from the given page in pdf
def get_df_from_pdf(bank, url, page, hasMultitable ):
    try:
        return read_pdf(url, pages=page, silent=True, multiple_tables=hasMultitable)
    except:
        print("THE LINK FOR {} HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE".format(bank.upper()))

#return a data_frame at particular postition in a pdf
def get_frame_by_coord(bank, url, coordinates, page):
    try:
        return read_pdf(url, pages=page,  area=coordinates, silent=True)
    except:
        print("THE LINK {} FOR HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE".format(bank.upper))

# return tabulate cordinate for object in a dict-positions
def compute_coord_from_object( positions, l_object):
    return [
                positions[l_object]["start"]["y"],
                positions[l_object]["start"]["x"],
                positions[l_object]["end"]["y"],
                positions[l_object]["end"]["x"]
            ]

#design for home loan
def home_loan_scraper(bank, b_data):
    print("{} HOME LOAN PROCESSING ...".format(bank))
    tab_col = ["PROVIDER", "CATEGORY", "CREDIT TYPE", "TERM", "RATE"]
    if b_data:
        # fileUtils.displayRates(tab_col, b_data)
        return processData(b_data, tab_col, "{} HOME LOANS".format(bank.upper()), "{}_hl_rates".format(bank.lower()))

#design for carrefour data
def process_crf_data(dataMatrix, tab_Column, directoryName, fileName):
    data_to_display = fileUtils.createNewFrame(dataMatrix, fileUtils.getFileContentAsList(fileName, directoryName))
    fileUtils.displayRates(tab_Column, data_to_display)
    return fileUtils.carrefourRatesUpdate(fileName, directoryName, dataMatrix, tab_Column, [])

