from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import os
from tabula import read_pdf
import requests
import numpy as np
import pandas as pd
from tabulate import tabulate
import json
import requests, PyPDF2, io
import re
import bs4
import sys
import time
from collections import namedtuple
import datetime
import os
import shutil
import urllib.request
import re
import csv
# import pdfbox


def bvbr():
    ###############################################################################################################
    ############################################BVBR0001###########################################################
    try:
        global bvbr_c
        df_bvbr1 = read_pdf('https://www.banquevanbreda.be/media/2675/tariefregeling-jvb-fr-293.pdf', encoding='ISO-8859-1',
                               pages=1, area=[156.83, 41.09, 229.28, 254.47], pandas_options={'header': None})
        df_bvbr0001 = df_bvbr1.drop(df_bvbr1.index[0])
        df_bvbr0001 = df_bvbr0001.drop(df_bvbr0001.columns[2:5], axis=1)
        df_bvbr0001.columns = ["Formules", "Taux"]
        df_bvbr0001["Formules"] = df_bvbr0001["Formules"].str.replace("Ã©", "é").str.strip()
        df_bvbr0001["Taux"] = df_bvbr0001["Taux"].str.replace("%", "").str.strip()
        Min_bvbr0001 = pd.DataFrame({'Min': ['', '0', '2', '4', '6', '11', '16']})
        Max_bvbr0001 = pd.DataFrame({'Max': ['', '1', '3', '5', '10', '15', '20']})
        duration_bvbr0001 = Min_bvbr0001.join(Max_bvbr0001)
        df_bvbr0001.insert(0, 'Provider', 'Banque Van Breda')
        df_bvbr0001.insert(0, 'Category', 'Home Loan')
        df_bvbr0001.insert(1, 'Product_ID', 'BVBR0001')
        df_bvbr0001 = df_bvbr0001.join(duration_bvbr0001)  # join newly made df with existed df
        df_bvbr0001 = df_bvbr0001[['Provider', 'Product_ID', 'Category', 'Formules', 'Min', 'Max', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################BVBR0002###########################################################
        df_bvbr2 = read_pdf('https://www.banquevanbreda.be/media/2675/tariefregeling-jvb-fr-293.pdf', encoding='ISO-8859-1',
                               pages=1, area=[234.04, 37.96, 286.35, 395.91], pandas_options={'header': None})

        df_bvbr0002 = df_bvbr2.drop(df_bvbr2.index[0]).drop(df_bvbr2.index[2:19])
        df_bvbr0002 = df_bvbr0002.drop(df_bvbr0002.columns[3:6], axis=1)
        df_bvbr0002.columns = ["__", "_", "Taux"]
        df_bvbr0002["Formules"] = df_bvbr0002["__"].map(str) + df_bvbr0002["_"].map(str)  # to join Name and CAP column
        df_bvbr0002.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0002.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0002["Formules"] = df_bvbr0002["Formules"].str.replace("Ã©", "é").str.strip()
        df_bvbr0002["Taux"] = df_bvbr0002["Taux"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0002 = pd.DataFrame({'Min': [''] * 1 + ['']})
        Max_bvbr0002 = pd.DataFrame({'Max': [''] * 1 + ['']})
        duration_bvbr0002 = Min_bvbr0002.join(Max_bvbr0002)

        df_bvbr0002.insert(0, 'Provider', 'Banque Van Breda')
        df_bvbr0002.insert(0, 'Category', 'Home Loan')
        df_bvbr0002.insert(1, 'Product_ID', 'BVBR0002')
        df_bvbr0002 = df_bvbr0002.join(duration_bvbr0002)  # join newly made df with existed df
        df_bvbr0002 = df_bvbr0002[['Provider', 'Product_ID', 'Category', 'Formules', 'Min', 'Max', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################BVBR0003###########################################################
        df_bvbr0003 = df_bvbr2.drop(df_bvbr2.index[0:4]).drop(df_bvbr2.index[5:19])
        df_bvbr0003 = df_bvbr0003.drop(df_bvbr0003.columns[3:6], axis=1)
        df_bvbr0003.columns = ["__", "_", "Taux"]
        df_bvbr0003["Formules"] = df_bvbr0003["__"].map(str) + df_bvbr0003["_"].map(str)  # to join Name and CAP column
        df_bvbr0003.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0003.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0003["Formules"] = df_bvbr0003["Formules"].str.replace("Ã©", "é").str.strip()
        df_bvbr0003["Taux"] = df_bvbr0003["Taux"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0003 = pd.DataFrame({'Min': [''] * 4 + ['']})
        Max_bvbr0003 = pd.DataFrame({'Max': [''] * 4 + ['']})
        duration_bvbr0003 = Min_bvbr0003.join(Max_bvbr0003)

        df_bvbr0003.insert(0, 'Provider', 'Banque Van Breda')
        df_bvbr0003.insert(0, 'Category', 'Home Loan')
        df_bvbr0003.insert(1, 'Product_ID', 'BVBR0003')
        df_bvbr0003 = df_bvbr0003.join(duration_bvbr0003)  # join newly made df with existed df
        df_bvbr0003 = df_bvbr0003[['Provider', 'Product_ID', 'Category', 'Formules', 'Min', 'Max', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################BVBR0004###########################################################

        df_bvbr0004 = df_bvbr2.drop(df_bvbr2.index[0:7]).drop(df_bvbr2.index[8:19])
        df_bvbr0004 = df_bvbr0004.drop(df_bvbr0004.columns[3:6], axis=1)
        df_bvbr0004.columns = ["__", "_", "Taux"]
        df_bvbr0004["Formules"] = df_bvbr0004["__"].map(str) + df_bvbr0004["_"].map(str)  # to join Name and CAP column
        df_bvbr0004.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0004.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0004["Formules"] = df_bvbr0004["Formules"].str.replace("Ã©", "é").str.strip()
        df_bvbr0004["Taux"] = df_bvbr0004["Taux"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0004 = pd.DataFrame({'Min': [''] * 7 + ['']})
        Max_bvbr0004 = pd.DataFrame({'Max': [''] * 7 + ['']})
        duration_bvbr0004 = Min_bvbr0004.join(Max_bvbr0004)

        df_bvbr0004.insert(0, 'Provider', 'Banque Van Breda')
        df_bvbr0004.insert(0, 'Category', 'Home Loan')
        df_bvbr0004.insert(1, 'Product_ID', 'BVBR0004')
        df_bvbr0004 = df_bvbr0004.join(duration_bvbr0004)  # join newly made df with existed df
        df_bvbr0004 = df_bvbr0004[['Provider', 'Product_ID', 'Category', 'Formules', 'Min', 'Max', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################BVBR0005###########################################################
        df_bvbr0005 = df_bvbr2.drop(df_bvbr2.index[0:10]).drop(df_bvbr2.index[11:19])
        df_bvbr0005 = df_bvbr0005.drop(df_bvbr0005.columns[3:6], axis=1)
        df_bvbr0005.columns = ["__", "_", "Taux"]
        df_bvbr0005["Formules"] = df_bvbr0005["__"].map(str) + df_bvbr0005["_"].map(str)  # to join Name and CAP column
        df_bvbr0005.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0005.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0005["Formules"] = df_bvbr0005["Formules"].str.replace("Ã©", "é").str.strip()
        df_bvbr0005["Taux"] = df_bvbr0005["Taux"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0005 = pd.DataFrame({'Min': [''] * 10 + ['']})
        Max_bvbr0005 = pd.DataFrame({'Max': [''] * 10 + ['']})
        duration_bvbr0005 = Min_bvbr0005.join(Max_bvbr0005)

        df_bvbr0005.insert(0, 'Provider', 'Banque Van Breda')
        df_bvbr0005.insert(0, 'Category', 'Home Loan')
        df_bvbr0005.insert(1, 'Product_ID', 'BVBR0005')
        df_bvbr0005 = df_bvbr0005.join(duration_bvbr0005)  # join newly made df with existed df
        df_bvbr0005 = df_bvbr0005[['Provider', 'Product_ID', 'Category', 'Formules', 'Min', 'Max', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################BVBR0006###########################################################
        df_bvbr0006 = df_bvbr2.drop(df_bvbr2.index[0:13]).drop(df_bvbr2.index[14:19])
        df_bvbr0006 = df_bvbr0006.drop(df_bvbr0006.columns[3:6], axis=1)
        df_bvbr0006.columns = ["__", "_", "Taux"]
        df_bvbr0006["Formules"] = df_bvbr0006["__"].map(str) + df_bvbr0006["_"].map(str)  # to join Name and CAP column
        df_bvbr0006.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0006.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0006["Formules"] = df_bvbr0006["Formules"].str.replace("Ã©", "é").str.strip()
        df_bvbr0006["Taux"] = df_bvbr0006["Taux"].str.replace("%", "").str.strip()

        # ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0006 = pd.DataFrame({'Min': [''] * 13 + ['']})
        Max_bvbr0006 = pd.DataFrame({'Max': [''] * 13 + ['']})
        duration_bvbr0006 = Min_bvbr0006.join(Max_bvbr0006)

        df_bvbr0006.insert(0, 'Provider', 'Banque Van Breda')
        df_bvbr0006.insert(0, 'Category', 'Home Loan')
        df_bvbr0006.insert(1, 'Product_ID', 'BVBR0006')
        df_bvbr0006 = df_bvbr0006.join(duration_bvbr0006)  # join newly made df with existed df
        df_bvbr0006 = df_bvbr0006[['Provider', 'Product_ID', 'Category', 'Formules', 'Min', 'Max', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################BVBR0007###########################################################
        df_bvbr0007 = df_bvbr2.drop(df_bvbr2.index[0:16]).drop(df_bvbr2.index[17:19])
        df_bvbr0007 = df_bvbr0007.drop(df_bvbr0007.columns[3:6], axis=1)
        df_bvbr0007.columns = ["__", "_", "Taux"]
        df_bvbr0007["Formules"] = df_bvbr0007["__"].map(str) + df_bvbr0007["_"].map(str)  # to join Name and CAP column
        df_bvbr0007.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0007.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0007["Formules"] = df_bvbr0007["Formules"].str.replace("Ã©", "é").str.strip()
        df_bvbr0007["Taux"] = df_bvbr0007["Taux"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0007 = pd.DataFrame({'Min': [''] * 16 + ['']})
        Max_bvbr0007 = pd.DataFrame({'Max': [''] * 16 + ['']})
        duration_bvbr0007 = Min_bvbr0007.join(Max_bvbr0007)

        df_bvbr0007.insert(0, 'Provider', 'Banque Van Breda')
        df_bvbr0007.insert(0, 'Category', 'Home Loan')
        df_bvbr0007.insert(1, 'Product_ID', 'BVBR0007')
        df_bvbr0007 = df_bvbr0007.join(duration_bvbr0007)  # join newly made df with existed df
        df_bvbr0007 = df_bvbr0007[['Provider', 'Product_ID', 'Category', 'Formules', 'Min', 'Max', 'Taux']]  # Change order of columns

        bvbr_c = pd.concat([
            pd.concat([df_bvbr0001], axis=1),
            pd.concat([df_bvbr0002], axis=1),
            pd.concat([df_bvbr0003], axis=1),
            pd.concat([df_bvbr0004], axis=1),
            pd.concat([df_bvbr0005], axis=1),
            pd.concat([df_bvbr0006], axis=1),
            pd.concat([df_bvbr0007], axis=1)])

        print(tabulate(bvbr_c, headers='keys', tablefmt='psql', showindex="never"))

    except:
        pass

are = [55.68*(72/25.4), 19.04*(72/25.4), 79.87*(72/25.4), 93.37*(72/25.4)]
a2 = [156.83, 41.09, 229.28, 254.47]
df_bvbr1 = read_pdf('https://www.banquevanbreda.be/media/2675/tariefregeling-jvb-fr-293.pdf', encoding='ISO-8859-1',
                       pages=1, area=are, pandas_options={'header': None})

print(df_bvbr1)