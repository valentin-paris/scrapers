import DataUtils
from  tabula import read_pdf
import requests, PyPDF2, io
# import requests
import camelot

# url_nege = 'https://www.nagelmackers.be/src/Frontend/Files/userfiles/files/Liste_des_tarifs_credits_logements.pdf'
# response_nege = requests.get(url_nege).text

# print(response_nege)

t ="https://www.nagelmackers.be/src/Frontend/Files/userfiles/files/Liste_des_tarifs_credits_logements.pdf"

# try:
#     data_as_frameList = read_pdf(t, pages= "1", silent=True,  multiple_tables=True )
# except:
#     print("THE LINK FOR ING HOME LOAN IS NOT AVAILABLE PLEASE CHECK ON THE WEB SITE")
#     data_as_frameList = None

# print(data_as_frameList)

# print(read_pdf(t, pages= "1", silent=True,  multiple_tables=True ))

# url_nege = 'https://www.nagelmackers.be/src/Frontend/Files/userfiles/files/Liste_des_tarifs_credits_logements.pdf'
# response_nege = requests.get(url_nege)

url = "https://www.nagelmackers.be/src/Frontend/Files/userfiles/files/Liste_des_tarifs_credits_logements.pdf"

headers = {
    'x-doing-ajax': "true",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "0277af77-2baf-4d95-a42a-c0cffcb575b2,b0988b41-1d3c-4667-a323-1752a90b7a2a",
    'Host': "www.nagelmackers.be",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)
print(response.status_code)
print(response.content)


with io.BytesIO(response.content) as open_pdf_file:
    print(open_pdf_file)
    print(PyPDF2.PdfFileReader(open_pdf_file).getPage(0).extractText())
    # print(read_pdf_nege.getPage(0))
# print(response.text)

# print(read_pdf(response.text))
#
# print(read_pdf("https://www.hellobank.be/docs/default-source/Products/h10061/fr-a.pdf"))
# print(read_pdf("https://www.nagelmackers.be/src/Frontend/Files/userfiles/files/Liste_des_tarifs_credits_logements.pdf",encoding='ISO-8859-1'))

# print(camelot.read_pdf(t))
# print(camelot.read_pdf("https://www.hellobank.be/docs/default-source/Products/h10061/fr-a.pdf"))

print([1,2,3,6] + [])