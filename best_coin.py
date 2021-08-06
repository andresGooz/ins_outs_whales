#se analizan las principales wallets de Dogecoin. De la 1 a la 700.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import pathlib
import datetime
from re import sub
from decimal import Decimal
import locale
import sys

def money(number):
    precio = 0
    try:
        number = str(number).replace('$','')
        number = ' '.join(number.split())
        number = number.split(",")
        precio += float(number[0].replace('.',''))
        try:
            precio += float("0."+number[1])
        except:
            pass
    except:
        precio = -1
    return precio

def considerar_row(row):
    lista = []
    coin_name = ' '.join(row.find_all("td")[2].find_all("div")[2].get_text().split())
    lista.append(coin_name)

    coin_price = row.find_all("td")[3].get_text()
    coin_price = money(coin_price)
    lista.append(coin_price)

    coin_market_cap = ' '.join(row.find_all("td")[8].get_text().split())
    coin_market_cap = float(coin_market_cap.replace('$','').replace('.',''))
    lista.append(coin_market_cap)

    coin_circulating_supply = float(coin_market_cap)/float(coin_price)
    lista.append(coin_circulating_supply)

    #mientras más grande sea esta relación, más puede crecer la moneda en cuestión.
    lista.append(coin_circulating_supply/coin_price)

    # print(lista)
    return lista

orden = 2
if (str(sys.argv[1]) == 'order_coin_market_cap'):
    orden = 2

if (str(sys.argv[1]) == 'supply_price_rate'):
    orden = 4


ins = 0
outs = 0
doges = 0
unsorted_list = []
for i in range(1, 4):
    url = 'https://www.coingecko.com/es?page='+str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all("tr")
    for row in table[1:]:
        unsorted_list.append(considerar_row(row))
unsorted_list.sort(key=lambda x:x[orden])
print(unsorted_list)
