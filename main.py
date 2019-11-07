import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from terminaltables import AsciiTable
from datetime import datetime

def get_stock(ticker):
    if isinstance(ticker, list):
        for x in ticker:
            current_stock_price(x)
            current_stock_summary(x)

    else:
        current_stock_summary(ticker)


def get_valuation(ticker):
    if isinstance(ticker, list):
        for x in ticker:
            current_stock_statistics(x)
    else:
        current_stock_statistics(ticker)

def get_wsj_movers():
    print("Work in progress")

def get_wsj_high_low():
    print("Work in progress")

def get_wsj_sectors():
    print("Work in progress")

def current_stock_price(ticker):
    url = "https://finance.yahoo.com/quote/{}".format(ticker)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.findAll('span')
    td = soup.find_all('td')
    now = datetime.now()

    price = str(span[13]).split(">")[1].split("<")[0]
    change = str(span[14]).split(">")[1].split("<")[0]
    print(f"\n\n{ticker} \nPrice: {price} \nChange:{change}\n")

def current_stock_summary(ticker):
    url = "https://finance.yahoo.com/quote/{}".format(ticker)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.findAll('span')
    td = soup.find_all('td')
    now = datetime.now()

    price = str(span[13]).split(">")[1].split("<")[0]
    change = str(span[14]).split(">")[1].split("<")[0]
    print(f"\n\n{ticker} \nPrice: {price} \nChange:{change}\n")

    if now.hour >= 16:
        prev_close = str(span[23]).split(">")[1].split("<")[0]
        prev_close_price = str(span[24]).split(">")[1].split("<")[0]

        open_ = str(span[25]).split(">")[1].split("<")[0]
        open_price = str(span[26]).split(">")[1].split("<")[0]

        bid = str(span[27]).split(">")[1].split("<")[0]
        bid_price = str(span[28]).split(">")[1].split("<")[0]

        ask = str(span[29]).split(">")[1].split("<")[0]
        ask_price = str(span[30]).split(">")[1].split("<")[0]

        day_range = str(span[31]).split(">")[1].split("<")[0]
        day_range_price = str(td[9]).split(">")[1].split("<")[0]

        week_range = str(span[32]).split(">")[1].split("<")[0]
        week_range_price = str(td[11]).split(">")[1].split("<")[0]
        print(week_range)

        volume = str(span[33]).split(">")[1].split("<")[0]
        volume_price = str(span[34]).split(">")[1].split("<")[0]

        avg_volume = str(span[35]).split(">")[1].split("<")[0]
        avg_volume_price = str(span[36]).split(">")[1].split("<")[0]

        market_cap = str(span[37]).split(">")[1].split("<")[0]
        market_cap_price = str(span[38]).split(">")[1].split("<")[0]

        beta = str(span[39]).split(">")[1].split("<")[0]
        beat_price = str(span[40]).split(">")[1].split("<")[0]

        pe = str(span[41]).split(">")[1].split("<")[0]
        pe_ratio = str(span[42]).split(">")[1].split("<")[0]

        eps = str(span[43]).split(">")[1].split("<")[0]
        eps_ratio = str(span[44]).split(">")[1].split("<")[0]

        table_date = [
        [ticker, 'Summary'],
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
        [eps, eps_ratio]
        ]
        table = AsciiTable(table_date)
        print(table.table)
    else:
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

        table_date = [
        [ticker, 'Summary'],
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
        [eps, eps_ratio]
        ]
        table = AsciiTable(table_date)
        print(table.table)


def current_stock_statistics(ticker):
    url = "https://finance.yahoo.com/quote/{}/key-statistics?p={}".format(ticker, ticker)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.findAll('span')
    td = soup.find_all('td')
    now = datetime.now()
    
    if now.hour >= 16:
        market_cap = str(span[15]).split(">")[1].split("<")[0]
        market_cap_price = str(td[1]).split(">")[1].split("<")[0]

        enterprise_value = str(span[16]).split(">")[1].split("<")[0]
        enterprise_value_price = str(td[3]).split(">")[1].split("<")[0]

        trailing_pe = str(span[17]).split(">")[1].split("<")[0]
        trailing_pe_num = str(td[5]).split(">")[1].split("<")[0]

        forward_pe = str(span[18]).split(">")[1].split("<")[0]
        forward_pe_num = str(td[7]).split(">")[1].split("<")[0]

        peg = str(span[19]).split(">")[1].split("<")[0]
        peg_ratio = str(td[9]).split(">")[1].split("<")[0]

        ps = str(span[20]).split(">")[1].split("<")[0]
        ps_ratio = str(td[11]).split(">")[1].split("<")[0]

        pb = str(span[21]).split(">")[1].split("<")[0]
        pb_ratio = str(td[13]).split(">")[1].split("<")[0]

        ev = str(span[22]).split(">")[1].split("<")[0]
        evr = str(td[15]).split(">")[1].split("<")[0]

        ebitda = str(span[23]).split(">")[1].split("<")[0]
        evebitda = str(td[17]).split(">")[1].split("<")[0]

        table_date = [
            [ticker, 'Valuation'],
            [market_cap, market_cap_price],
            [enterprise_value,enterprise_value_price],
            [trailing_pe, trailing_pe_num],
            [forward_pe, forward_pe_num],
            [peg, peg_ratio],
            [ps, ps_ratio],
            [pb, pb_ratio],
            [ev, evr],
            [ebitda, evebitda]
        ]
        table = AsciiTable(table_date)
        print(table.table)
    else: 
        market_cap = str(span[15]).split(">")[1].split("<")[0]
        market_cap_price = str(td[1]).split(">")[1].split("<")[0]

        enterprise_value = str(span[16]).split(">")[1].split("<")[0]
        enterprise_value_price = str(td[3]).split(">")[1].split("<")[0]

        trailing_pe = str(span[17]).split(">")[1].split("<")[0]
        trailing_pe_num = str(td[5]).split(">")[1].split("<")[0]

        forward_pe = str(span[18]).split(">")[1].split("<")[0]
        forward_pe_num = str(td[7]).split(">")[1].split("<")[0]

        peg = str(span[19]).split(">")[1].split("<")[0]
        peg_ratio = str(td[9]).split(">")[1].split("<")[0]

        ps = str(span[20]).split(">")[1].split("<")[0]
        ps_ratio = str(td[11]).split(">")[1].split("<")[0]

        pb = str(span[21]).split(">")[1].split("<")[0]
        pb_ratio = str(td[13]).split(">")[1].split("<")[0]

        ev = str(span[22]).split(">")[1].split("<")[0]
        evr = str(td[15]).split(">")[1].split("<")[0]

        ebitda = str(span[23]).split(">")[1].split("<")[0]
        evebitda = str(td[17]).split(">")[1].split("<")[0]

        table_date = [
            [ticker, 'Valuation'],
            [market_cap, market_cap_price],
            [enterprise_value,enterprise_value_price],
            [trailing_pe, trailing_pe_num],
            [forward_pe, forward_pe_num],
            [peg, peg_ratio],
            [ps, ps_ratio],
            [pb, pb_ratio],
            [ev, evr],
            [ebitda, evebitda]
        ]
        table = AsciiTable(table_date)
        print(table.table)
