#se analizan las principales wallets de Dogecoin. De la 1 a la 700.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import pathlib
import datetime

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

ins = 0
outs = 0
doges = 0

for i in range(1, 2):
    url = 'https://bitinfocharts.com/top-100-richest-dogecoin-addresses-'+str(i)+'.html'
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

print("DATETIME: " + str(datetime.datetime.now()))
print("INS: " + f"{ins:,}")
print("OUTS: " + f"{outs:,}")
print("DOGES: " + f"{doges:,}")
