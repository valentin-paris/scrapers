import fileUtils
from tabula import read_pdf

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

#create a 2x2 list of data from group dict structure
def formatDataFrom(groups, provider):
    frameToExport = []
    for eachGroup in groups:
        frameToExport.append([provider, eachGroup[3], eachGroup[0], min(map(int, groups[eachGroup])),
                              max(map(int, groups[eachGroup])), int(eachGroup[1]), float(eachGroup[2])])
    return frameToExport

def addAtributes(loanList, lType, duration, rate, pdtID):
    for loan in loanList:
        loan['type'] = lType
        loan['duration'] = duration
        loan['rate'] = rate
        loan['productID'] = pdtID

#to compute coordinate from mm to px for pdf scraped file
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

# return tabulate coordinates for object in a dict-positions
def compute_coord_from_object( positions, l_object):
    return [
                positions[l_object]["start"]["y"],
                positions[l_object]["start"]["x"],
                positions[l_object]["end"]["y"],
                positions[l_object]["end"]["x"]
            ]

#perform the data comparison and the file operations for data that doens't need to be grouped
#dataMatrix is a 2x2 list of data
def processData(dataMatrix, tab_Column, directoryName, fileName):
    if dataMatrix:
        fileUtils.displayRates(tab_Column, dataMatrix)
        return fileUtils.upToDate(fileName, directoryName, dataMatrix, tab_Column)
    else:
        return None

#define a more generic function to process the data with grouping of data for large dataset
def proc_data(b_data, provider, dir_name, file_name, tab_col):
    data_matrix = formatDataFrom(createGroups(b_data), provider)
    if data_matrix:
        fileUtils.displayRates(tab_col, data_matrix)
        return fileUtils.upToDate(file_name, dir_name, data_matrix, tab_col)
    else:
        return None

#design for home loan to handle exceptions
def home_loan_scraper(bank, b_data):
    tab_col = ["PROVIDER", "CATEGORY", "CREDIT TYPE", "TERM", "RATE"]
    if b_data:
        try:
            print("{} HOME LOAN PROCESSING ...".format(bank))
            # fileUtils.displayRates(tab_col, b_data)
            return processData(b_data, tab_col, "{} HOME LOANS".format(bank.upper()), "{}_hl_rates".format(bank.lower()))
        except:
            print("THE STRUCTURE OF {} HOME LOAN PDF HAS BEEN MODIFIED PLEASE PROCESS IT BACK!".format(bank))

#design for carrefour data
def process_crf_data(dataMatrix, tab_Column, directoryName, fileName):
    data_to_display = fileUtils.createNewFrame(dataMatrix, fileUtils.getFileContentAsList(fileName, directoryName))
    fileUtils.displayRates(tab_Column, data_to_display)
    return fileUtils.carrefourRatesUpdate(fileName, directoryName, dataMatrix, tab_Column, [])

'''
            perform the scraping for an individual bank and send notification
            
file_to_mail --> is a list of file path i.e the result of the scrape procedure 
bank --> is a string representing the bank_name
mail_list --> is a list of email adresses

                     exemple usage  for argenta 
scrape_and_notify(scraper(), "ARGENTA HOME LOANS", ["email01@domain.be", email02@domain.be])
'''
def scrape_and_notify(file_to_email, bank, mail_list):
    if file_to_email:
        message = ["{} UPDATED ITS RATES A FILE IS ATTACHED WITH UP TO DATE RATES".format(bank.upper())]
        fileUtils.send_email_to(mail_list, "{} SCRAPE".format(bank.upper()), message, file_to_email)
    else:
        message = ["{} SCRAPE EXECUTED SUCCESSFULLY.".format(bank.upper()), "RATES ARE UP TO DATE."]
        fileUtils.send_email_to(mail_list, "{} SCRAPE".format(bank.upper()), message, file_to_email)

