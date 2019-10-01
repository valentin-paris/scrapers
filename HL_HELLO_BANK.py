import DataUtils

pdf_link = "https://www.hellobank.be/docs/default-source/Products/h10061/fr-a.pdf"
positions = {
    "fix_rate": {
        "start": {
            "x": DataUtils.cpt(23),
            "y": DataUtils.cpt(105)

        },
        "end": {
            "x": DataUtils.cpt(136),
            "y": DataUtils.cpt(161)
        }
    }
}

def bankData():
    bankData = []
    for l_type in positions:
        l_data = DataUtils.get_frame_by_coord(
            "hello bank", pdf_link, DataUtils.compute_coord_from_object(positions, l_type), 1).values.tolist()
        for line in l_data:
            bankData.append(["HELLO BANK", "HOME LOAN", l_type, line[0], line[1]])
    return bankData

def scraper():
    return DataUtils.home_loan_scraper("hello bank", bankData())


scraper()