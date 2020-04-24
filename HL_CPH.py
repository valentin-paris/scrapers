import tabula
import DataUtils

# import fileUtils

try:
    data_as_frameList = tabula.read_pdf(
        "https://www.cph.be/images/stories/PDF/tarif_cph_logement_20190901.pdf",
        pages="all", silent=True, multiple_tables=True)
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
    return DataUtils.home_loan_scraper("CPH", bank_data())

# scraper()
