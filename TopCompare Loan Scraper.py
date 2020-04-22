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
from app_rating import compare_rate_and_notify
#from app_score_update_csv import update_score_csv


from app_rating import app_rate_frame
import datetime
import os.path


mailList = ["valentin.paris@topcompare.be", "jihane.elkhyari@topcompare.be"]
mailTest = ["bernaud.toukam@topcompare.be"]
console_file = "console_output.txt"

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
    import sys
    sys.stdout = open(console_file, 'w')
    filesToBeMailed = []
    generalMessage = []
    for bank in tcBanksScrapers:
        try:
            newData = tcBanksScrapers[bank]()
            filesToBeMailed += newData
            if newData:
                generalMessage += ['{}... UPDATED.'.format(bank)]
        except:
            generalMessage += ['{}... ERROR .'.format(bank)]
    if not generalMessage:
        generalMessage += ['the scraper executed sucessfully and there is no change in the rates!']
    else:
        generalMessage = ["BANK RATES STATUS", ""] + generalMessage
    generalMessage += ["", "LINKS STATUS: "] + check_links() + compare_rate_and_notify(0.25)
    # print(filesToBeMailed, generalMessage)
    sys.stdout.close()
    filesToBeMailed += [fileUtils.get_console_file(console_file)]
    fileUtils.send_email_to(mailList, 'daily scrape', generalMessage, filesToBeMailed)




def update_score_csv() :
    max_days_for_update = 7
    csv_file_path = "./app_score.csv"
    if not(os.path.isfile(csv_file_path)):
        csv_file = open(csv_file_path, "w")
        csv_file.write("DATE;BANK;SCORE\n")
        csv_file.close()

    with open(csv_file_path, 'r') as csv_file:
        last_line = csv_file.read().splitlines()[-1]

    should_update = False
    try:
        last_date = last_line.split(';', 1)[0]
        last_date = datetime.datetime.strptime(last_date, "%m/%d/%y").date()
        diff = (last_date - datetime.date.today()).days
        if(abs(diff) >= max_days_for_update):
            should_update = True
    except:
        should_update = True

    if(not(should_update)):
        return False

    rate = app_rate_frame()
    csv_file = open(csv_file_path, "a")
    cur_date = datetime.date.today().strftime("%m/%d/%y")

    for bank_score in rate:
        line = cur_date + ";" + bank_score[0] + ";" + str(bank_score[5])+"\n"
        csv_file.write(line)

    csv_file.close()

    
update_score_csv()
tcLoanScrape()














