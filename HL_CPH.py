import tabula
import DataUtils
# import fileUtils

try:
    data_as_frameList = tabula.read_pdf("https://www.cph.be/images/stories/PDF/tarif_cph_logement_20190901.pdf#view=fitV",
                                        pages= "all", silent=True,  multiple_tables=True )
except:
    print("THE LINK FOR CPH HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
    data_as_frameList = None

def bank_data():
    bank_data = []
    fix_rate_data = data_as_frameList[0].values.tolist()
    variable_rate_data = data_as_frameList[1].values.tolist()
    for line in fix_rate_data:
        bank_data.append(["CPH", "HOME LOAN", "FIX RATE", line[0], line[1]])
    for line in variable_rate_data:
        bank_data.append(["CPH", "HOME LOAN", line[0], "-", line[1]])
    return bank_data

def scraper():
    print("CPH HOME LOAN PROCESSING ...")
    tab_col = ["PROVIDER", "CATEGORY", "CREDIT TYPE", "TERM", "RATE"]
    data_matrix = bank_data()
    if data_matrix:
        # fileUtils.displayRates(tab_col, data_matrix)
        return DataUtils.processData(data_matrix, tab_col, "BVBR HOME LOANS", "bvbr_hl_rates")

scraper()