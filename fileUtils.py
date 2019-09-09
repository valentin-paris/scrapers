from tabulate import tabulate
import pandas as pd
import os
import time
import datetime
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ntpath


# displays list as lisible tableau
def displayRates(colonnes, content):
    print(tabulate(
        pd.DataFrame(content, columns=colonnes),
        headers='keys', tablefmt='psql', showindex="never"))


# create a custom name for the file
def computeFileName(name):
    return "{}_{}.csv".format(name, time.strftime("%Y-%m-%d %H.%M.%S"))
    # return "{}_{}.csv".format(name, datetime.datetime.now())


# check if the folder exists and create it if not
def checkToCreate(dirName):
    final_path = os.path.join(os.getcwd(), dirName)
    if not os.path.exists(final_path):
        os.makedirs(final_path)


# export a dataFrame from ListData as csv in a given folder
def exportListToCsv(listData, tableColumns, directoryName, fileName):
    checkToCreate(directoryName)
    name = computeFileName(fileName)
    frame = pd.DataFrame(listData, columns=tableColumns)
    frame.to_csv(os.path.join(os.getcwd(), directoryName, name), index=False)


# compare csv file content with list content and returns the difference
def compareFileAndList(fichier, directory, todayScrape):
    frame = pd.read_csv(os.path.join(os.getcwd(), directory, fichier))
    currentContent = frame.values.tolist()
    return [lines for lines in todayScrape if (lines not in currentContent)]


# export a content to update file as csv
def createUpdate(dirName, fileName, dataContent, tableColumns):
    newName = '{}_{}'.format(fileName, 'update')
    updatePath = '{}\{}_{}'.format(dirName, fileName, 'update')
    exportListToCsv(dataContent, tableColumns, updatePath, newName)


# move the current scrapeFile to history file
def moveToHistory(dirName, fileNamne, file):
    historyPath = '{}\{}_{}'.format(dirName, fileNamne, 'History')
    checkToCreate(historyPath)
    os.rename(os.path.join(os.getcwd(), dirName, file), os.path.join(os.getcwd(), historyPath, file))


# update the directory with file in case of change
# dailyScrape schould be a matrix ie list of list
def upToDate(fileName, dirName, dailyScrape, tabColumns, fileForEmail):
    checkToCreate(dirName)
    found = False
    # if the folder is not empty
    if os.listdir(os.path.join(os.getcwd(), dirName)):
        for fichier in os.listdir(os.path.join(os.getcwd(), dirName)):
            # check if the file exists and get its right name
            if os.path.isfile(os.path.join(os.getcwd(), dirName, fichier)) and fichier.startswith(fileName):
                newData = compareFileAndList(fichier, dirName, dailyScrape)
                if newData:
                    createUpdate(dirName, fileName, newData, tabColumns)
                    moveToHistory(dirName, fileName, fichier)
                    exportListToCsv(dailyScrape, tabColumns, dirName, fileName)
                    fileForEmail.append(getLatestUpdate(dirName, fileName))
                found = True
        if not found:
            exportListToCsv(dailyScrape, tabColumns, dirName, fileName)
    else:
        exportListToCsv(dailyScrape, tabColumns, dirName, fileName)
    return fileForEmail


# returns the most recent csv file in the update directory
def getLatestUpdate(directory, name):
    if os.path.exists(os.path.join(os.getcwd(), directory, "{}_{}".format(name, 'update'))):
        # returns the file with max value in terms of time "key" in the folder path glob.glob gives the list of files
        list_of_files = glob.glob(os.path.join(os.getcwd(), directory, "{}_{}".format(name, 'update'), '*.csv'))
        return max(list_of_files, key=os.path.getctime)


# send a mail with potentially attached file
def send_email_to(send_to, subject, message, filesToAttach):
    for mailUser in send_to:
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login('tcdailyscrape@gmail.com', 'donotreply0001')
        msg = MIMEMultipart()
        msg['From'] = 'tcdailyscrape@gmail.com'
        msg['To'] = mailUser
        msg['Subject'] = subject

        # add in the message body
        msg.attach(MIMEText(str('\n'.join(message)), 'plain'))

        if filesToAttach:
            for filename in filesToAttach:
                # attachment = open(os.path.join(os.getcwd(), directory, filename), "rb")
                attachment = open(filename, "rb")

                # instance of MIMEBase and named as p
                p = MIMEBase('application', 'octet-stream')

                # To change the payload into encoded form
                p.set_payload(attachment.read())

                # encode into base64
                encoders.encode_base64(p)

                # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                p.add_header('Content-Disposition', "attachment", filename=ntpath.basename(filename))

                # attach the instance 'p' to instance 'msg'
                msg.attach(p)

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg

        # Terminate the SMTP session and close the connection
        s.quit()








