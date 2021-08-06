import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import pathlib
import datetime
import csv
import sys


def sumar_row(ins, outs, doges, row):
    try:
        a_string = str(row.find_all("td")[2].get_text()).split(" ")[0]
        numeric_string = re.sub("[^0-9]", "", a_string)
        doges += int(numeric_string)
    except:
        pass
    try:
        ins += int(row.find_all("td")[-1].get_text())
    except:
        pass
    try:
        outs += int(row.find_all("td")[-4].get_text())
    except:
        pass
    return ins, outs, doges

#++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++
# START PANEL DE CONFIGURACIÓN CENTRAL
currency_list = ['bitcoin' , 'dogecoin']
hasta_list = [100, 200]
# settings.
# 1 vez al día ejecutar los comandos en las configuraciones 00 01 10 11
selected_currency = str(sys.argv[1])
hasta = int(sys.argv[2])

# END
#++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++

ins = 0
outs = 0
doges = 0
hasta = int(hasta/100)
for i in range(1, hasta+1):
    url = 'https://bitinfocharts.com/top-100-richest-' + selected_currency + '-addresses-' + str(i) + '.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all("table", {"class": "table-striped"})

    for table in tables:
        try:
            for row in table.find("tbody"):
                ins, outs, doges = sumar_row(ins, outs, doges, row)
        except:
            for row in table:
                ins, outs, doges = sumar_row(ins, outs, doges, row)

f = open('file.csv', 'a')
writer = csv.writer(f)
writer.writerow([str(datetime.datetime.now()), selected_currency, "[1, "+ str(hasta) + "00]", doges, ins, outs])
f.close()
