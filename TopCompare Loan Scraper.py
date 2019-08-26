import test_data
# import ING_Rates
# import KBC_Rates
# import DHB_Bank_Rates
# import CPH_Rates
import fileUtils


# tcBanksScrapers = {
#     'ING': ING_Rates.iNGLoanscraper(),
#     'KBC': KBC_Rates.kBC_loan_scrape(),
#     'DHB_Bank': DHB_Bank_Rates.dHBLoanScraper(),
#     'CPH_Bank': CPH_Rates.cphLoansScraper()
# }

tcBanksScrapers = {
    'TEST': test_data.scrapeTest,
    'TEST2': test_data.sectest
}


#DHB IS CAUSING SOME TROUBLE IT CRACHES FOR THE 1ST TWO TRY AND START WORK AFTER THE 3RD
#REASON: the website is sending incomplete data during the 1st and second scrape
#the procedure has to ignore the potential exeptions that could be thrown during the firt try
def tcLoanScrape():
    filesToBeMailed = []
    generalMessage = []
    for bank in tcBanksScrapers:
        if bank == 'DHB_Bank':
            try:
                newData = tcBanksScrapers[bank]()
                filesToBeMailed += newData
                if newData:
                    generalMessage += ['{} updated its rates, a file is attached with up to date rates.'.format(bank)]
            except:
                i = 3
                while i > 0:
                    try:
                        newData = tcBanksScrapers[bank]()
                        filesToBeMailed += newData
                        if newData:
                            generalMessage += [
                                '{} updated its rates, a file is attached with up to date rates.'.format(bank)]
                        i = 0
                    except:
                        i -= 1
                        if i == 0:
                            generalMessage += ['an error occured with {} scrape'.format(bank)]
        else:

            try:
                newData = tcBanksScrapers[bank]()
                filesToBeMailed += newData
                if newData:
                    generalMessage += ['{} updated its rates, a file is attached with up to date rates.'.format(bank)]
            except:
                generalMessage += ['an error occured with {} scrape'.format(bank)]
    if not generalMessage:
        generalMessage += ['the scraper executed sucessfully and there is no change in the rates!']
    fileUtils.send_email_to('paulbernaud@yahoo.fr', 'daily scrape', generalMessage, filesToBeMailed)
    print(filesToBeMailed, generalMessage)


tcLoanScrape()









