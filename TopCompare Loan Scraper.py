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
import BPOST_Loan_Rates
import Europa_Bank_Rates
import Elantis_rates
import Santander_rates
import BNPPF_Loan_Rates
import Cofidis_rates
import HL_Argenta
import HL_Belfius
import HL_BNPPF
import HL_BVBR
import HL_CBC
import HL_CPH
import HL_FEDERALE_ASS
import HL_HELLO_BANK
import HL_ING
import HL_KBC
import HL_BPOST
from link_tracker import check_links


mailList = ['alerts@topcompare.be', 'quentin@topcompare.be', "bernaud.toukam@topcompare.be"]
mailTest = ["bernaud.toukam@topcompare.be"]

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
    'CETELEM': Cetelem_Rates_Scraper.cetelemLoanScraper,
    'BPOST': BPOST_Loan_Rates.bpostLoanScraper,
    'EUROPA BANK': Europa_Bank_Rates.europaLoanScraper,
    'ELANTIS': Elantis_rates.elantisLoanScraper,
    'SANTANDER': Santander_rates.santanderLoanScraper,
    'BNPPF': BNPPF_Loan_Rates.scraper,
    "COFIDIS": Cofidis_rates.cofidisLoanScraper,
    "HOME LOAN ARGENTA": HL_Argenta.scraper,
    "HOME LOAN BELFIUS": HL_Belfius.scraper,
    "HOME LOAN BNPPF": HL_BNPPF.scraper,
    "HOME LOAN BVBR": HL_BVBR.scraper,
    "HOME LOAN CBC": HL_CBC.scraper,
    "HOME LOAN CPH": HL_CPH.scraper,
    "HOME LOAN FEDERALE ASSUR": HL_FEDERALE_ASS.scraper,
    "HOME LOAN HELLO BANK": HL_HELLO_BANK.scraper,
    "HOME LOAN ING": HL_ING.scraper,
    "HOME LOAN KBC": HL_KBC.scraper,
    "HOME LOAN BPOST": HL_BPOST.scraper
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
            generalMessage += ['an error occured with {} scrape, please check the console for more informations.'.format(bank)]
    if not generalMessage:
        generalMessage += ['the scraper executed sucessfully and there is no change in the rates!']
    generalMessage += ["LINKS STATUS: "] + check_links()
    fileUtils.send_email_to(mailTest, 'daily scrape', generalMessage, filesToBeMailed)
    print(filesToBeMailed, generalMessage)

tcLoanScrape()












