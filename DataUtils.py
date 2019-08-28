import fileUtils

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




