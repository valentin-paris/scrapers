import fileUtils
import ING_Rates
import KBC_Rates
import DHB_Bank_Rates
import Bank_Carrefour_Rates
import CPH_Rates
import CBC_Loan_Rates
import Axa_Int_Rates
import Crelan_Rates
import HelloBank_Rates
import Cetelem_Rates_Scraper



tcBanksScrapers = {
    'ING': ING_Rates.iNGLoanscraper,
    'KBC': KBC_Rates.kBC_loan_scrape,
    'DHB_Bank': DHB_Bank_Rates.dHBLoanScraper,
    'CPH_Bank': CPH_Rates.cphLoansScraper,
    'CARREFOUR_BANK': Bank_Carrefour_Rates.carrefourLoanScraper,
    'CBC_BANK': CBC_Loan_Rates.cbcLoanScraper,
    'AXA': Axa_Int_Rates.axaLoanScraper, 
    'CRELAN': Crelan_Rates.crelanLoansScraper,
    'HELLO BANK': HelloBank_Rates.helloBankScraper,
    'CETELEM': Cetelem_Rates_Scraper.cetelemLoanScraper
}

def tcLoanScrape():
    filesToBeMailed = []
    generalMessage = []
    for bank in tcBanksScrapers:
        try:
            newData = tcBanksScrapers[bank]()
            filesToBeMailed += newData
            if newData:
                generalMessage += ['{} updated its rates, a file is attached with up to date rates.'.format(bank)]
        except:
            generalMessage += ['an error occured with {} scrape'.format(bank)]
    if not generalMessage:
        generalMessage += ['the scraper executed sucessfully and there is no change in the rates!']
    fileUtils.send_email_to(['alerts@topcompare.com', "paulbernaud@yahoo.fr"], 'daily scrape', generalMessage, filesToBeMailed)
    print(filesToBeMailed, generalMessage)


tcLoanScrape()











