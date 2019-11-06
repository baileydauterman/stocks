import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from terminaltables import AsciiTable

def get_price(ticker):
    url = "https://finance.yahoo.com/quote/{}".format(ticker)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.findAll('span')
    price = str(span[13]).split(">")[1].split("<")[0]
    change = str(span[14]).split(">")[1].split("<")[0]
    print(f"{ticker} \nPrice: {price} \nChange:{change}")

def get_value(ticker):
    url = "https://finance.yahoo.com/quote/{}".format(ticker)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.findAll('span')
    td = soup.find_all('td')

    prev_close = str(span[18]).split(">")[1].split("<")[0]
    prev_close_price = str(span[19]).split(">")[1].split("<")[0]

    open_ = str(span[20]).split(">")[1].split("<")[0]
    open_price = str(span[21]).split(">")[1].split("<")[0]

    bid = str(span[22]).split(">")[1].split("<")[0]
    bid_price = str(span[23]).split(">")[1].split("<")[0]

    ask = str(span[24]).split(">")[1].split("<")[0]
    ask_price = str(span[25]).split(">")[1].split("<")[0]

    day_range = str(span[26]).split(">")[1].split("<")[0]
    day_range_price = str(td[9]).split(">")[1].split("<")[0]

    week_range = str(span[28]).split(">")[1].split("<")[0]
    week_range_price = str(td[11]).split(">")[1].split("<")[0]

    volume = str(span[30]).split(">")[1].split("<")[0]
    volume_price = str(span[31]).split(">")[1].split("<")[0]

    avg_volume = str(span[32]).split(">")[1].split("<")[0]
    avg_volume_price = str(span[33]).split(">")[1].split("<")[0]

    market_cap = str(span[34]).split(">")[1].split("<")[0]
    market_cap_price = str(span[35]).split(">")[1].split("<")[0]

    beta = str(span[36]).split(">")[1].split("<")[0]
    beat_price = str(span[37]).split(">")[1].split("<")[0]

    pe = str(span[38]).split(">")[1].split("<")[0]
    pe_ratio = str(span[39]).split(">")[1].split("<")[0]

    eps = str(span[40]).split(">")[1].split("<")[0]
    eps_ratio = str(span[41]).split(">")[1].split("<")[0]

    yr_target = str(span[44]).split(">")[1].split("<")[0]
    yr_target_price = str(span[45]).split(">")[1].split("<")[0]

    table_date = [
        [ticker, ''],
        [prev_close, prev_close_price],
        [open_,open_price],
        [bid, bid_price],
        [ask, ask_price],
        [day_range, day_range_price],
        [week_range, week_range_price],
        [volume, volume_price],
        [avg_volume, avg_volume_price],
        [market_cap, market_cap_price],
        [beta, beat_price],
        [pe, pe_ratio],
        [eps, eps_ratio],
        [yr_target, yr_target_price]
    ]
    table = AsciiTable(table_date)
    print(table.table)
