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

def get_movers():
    daily_gainers()
    daily_losers()
    
def get_esg(ticker):
    esg(ticker)

def get_key_stats():
    key_stats()

def get_sectors():
    sectors()

def current_stock_price(ticker):
    url = "https://finance.yahoo.com/quote/{}".format(ticker)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.findAll('span')

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
        
def esg(ticker):
    url = "https://finance.yahoo.com/quote/{}/sustainability".format(ticker)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.findAll('span')
    div = soup.find_all('div')

    if len(span) < 50:
        print(f"{ticker} has no sustainability data on Yahoo Finance")
    else:
        performance = str(span[17]).split(">")[1].split("<")[0]
        print(f"\n\n{ticker}: {performance}\n\n")

        total_esg = "Total ESG Score"
        total_esg_score = str(div[66]).split(">")[1].split("<")[0]
        total_esg_percentile = str(span[16]).split(">")[1].split("<")[0]

        environmental = "Environment"
        enviro_esg_score = str(div[76]).split(">")[1].split("<")[0]
        enviro_esg_percentile = str(span[21]).split(">")[1].split("<")[0]

        social = "Social"
        social_esg_score = str(div[83]).split(">")[1].split("<")[0]
        social_esg_percentile = str(span[24]).split(">")[1].split("<")[0]

        gov = "Governance"
        gov_esg_score = str(div[90]).split(">")[1].split("<")[0]
        gov_esg_percentile = str(span[27]).split(">")[1].split("<")[0]
        
        table_date = [
            ['Indicator', 'Score','Percentile'],
            [total_esg,total_esg_score,total_esg_percentile],
            [environmental,enviro_esg_score,enviro_esg_percentile],
            [social,social_esg_score,social_esg_percentile],
            [gov,gov_esg_score,gov_esg_percentile]
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

def daily_gainers():
    url = "https://money.cnn.com/data/hotstocks/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.find_all('span')
    a = soup.find_all('a')

    print("\n\n------GAINERS------\n")

    first_ticker = str(a[86]).split(">")[1].split("<")[0]
    first = str(span[81]).split(">")[1].split("<")[0]
    first_price = str(span[82]).split(">")[1].split("<")[0]
    first_change = str(span[84]).split(">")[1].split("<")[0]
    first_per_change = str(span[86]).split(">")[1].split("<")[0]

    second_ticker = str(a[87]).split(">")[1].split("<")[0]
    second = str(span[87]).split(">")[1].split("<")[0]
    second_price = str(span[88]).split(">")[1].split("<")[0]
    second_change = str(span[90]).split(">")[1].split("<")[0]
    second_per_change = str(span[92]).split(">")[1].split("<")[0]

    third_ticker = str(a[88]).split(">")[1].split("<")[0]
    third = str(span[93]).split(">")[1].split("<")[0]
    third_price = str(span[94]).split(">")[1].split("<")[0]
    third_change = str(span[96]).split(">")[1].split("<")[0]
    third_per_change = str(span[98]).split(">")[1].split("<")[0]

    fourth_ticker = str(a[89]).split(">")[1].split("<")[0]
    fourth = str(span[99]).split(">")[1].split("<")[0]
    fourth_price = str(span[100]).split(">")[1].split("<")[0]
    fourth_change = str(span[102]).split(">")[1].split("<")[0]
    fourth_per_change = str(span[104]).split(">")[1].split("<")[0]

    fifth_ticker = str(a[90]).split(">")[1].split("<")[0]
    fifth = str(span[105]).split(">")[1].split("<")[0]
    fifth_price = str(span[106]).split(">")[1].split("<")[0]
    fifth_change = str(span[108]).split(">")[1].split("<")[0]
    fifth_per_change = str(span[110]).split(">")[1].split("<")[0]

    sixth_ticker = str(a[91]).split(">")[1].split("<")[0]
    sixth = str(span[111]).split(">")[1].split("<")[0]
    sixth_price = str(span[112]).split(">")[1].split("<")[0]
    sixth_change = str(span[114]).split(">")[1].split("<")[0]
    sixth_per_change = str(span[116]).split(">")[1].split("<")[0]

    seven_ticker = str(a[92]).split(">")[1].split("<")[0]
    seven = str(span[117]).split(">")[1].split("<")[0]
    seven_price = str(span[118]).split(">")[1].split("<")[0]
    seven_change = str(span[120]).split(">")[1].split("<")[0]
    seven_per_change = str(span[122]).split(">")[1].split("<")[0]

    eight_ticker = str(a[93]).split(">")[1].split("<")[0]
    eight = str(span[123]).split(">")[1].split("<")[0]
    eight_price = str(span[124]).split(">")[1].split("<")[0]
    eight_change = str(span[126]).split(">")[1].split("<")[0]
    eight_per_change = str(span[128]).split(">")[1].split("<")[0]

    nine_ticker = str(a[94]).split(">")[1].split("<")[0]
    nine = str(span[129]).split(">")[1].split("<")[0]
    nine_price = str(span[130]).split(">")[1].split("<")[0]
    nine_change = str(span[132]).split(">")[1].split("<")[0]
    nine_per_change = str(span[134]).split(">")[1].split("<")[0]

    ten_ticker = str(a[95]).split(">")[1].split("<")[0]
    ten = str(span[135]).split(">")[1].split("<")[0]
    ten_price = str(span[136]).split(">")[1].split("<")[0]
    ten_change = str(span[138]).split(">")[1].split("<")[0]
    ten_per_change = str(span[140]).split(">")[1].split("<")[0]

    table_date = [
        ['Ticker', 'Company', 'Price', 'Change', '% Change'],
        [first_ticker, first, first_price, first_change, first_per_change],
        [second_ticker, second, second_price, second_change, second_per_change],
        [third_ticker, third, third_price, third_change, third_per_change],
        [fourth_ticker, fourth, fourth_price, fourth_change, fourth_per_change],
        [fifth_ticker, fifth, fifth_price, fifth_change, fifth_per_change],
        [sixth_ticker, sixth, sixth_price, sixth_change, sixth_per_change],
        [seven_ticker, seven, seven_price, seven_change, seven_per_change],
        [eight_ticker, eight, eight_price, eight_change, eight_per_change],
        [nine_ticker, nine, nine_price, nine_change, nine_per_change],
        [ten_ticker, ten, ten_price, ten_change, ten_per_change]
    ]
    table = AsciiTable(table_date)
    print(table.table)

def daily_losers():
    url = "https://money.cnn.com/data/hotstocks/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.find_all('span')
    a = soup.find_all('a')

    print("\n\n------LOSERS-------\n")
    
    first_ticker = str(a[96]).split(">")[1].split("<")[0]
    first = str(span[142]).split(">")[1].split("<")[0]
    first_price = str(span[143]).split(">")[1].split("<")[0]
    first_change = str(span[145]).split(">")[1].split("<")[0]
    first_per_change = str(span[147]).split(">")[1].split("<")[0]

    second_ticker = str(a[97]).split(">")[1].split("<")[0]
    second = str(span[148]).split(">")[1].split("<")[0]
    second_price = str(span[149]).split(">")[1].split("<")[0]
    second_change = str(span[151]).split(">")[1].split("<")[0]
    second_per_change = str(span[153]).split(">")[1].split("<")[0]

    third_ticker = str(a[98]).split(">")[1].split("<")[0]
    third = str(span[154]).split(">")[1].split("<")[0]
    third_price = str(span[155]).split(">")[1].split("<")[0]
    third_change = str(span[157]).split(">")[1].split("<")[0]
    third_per_change = str(span[159]).split(">")[1].split("<")[0]

    fourth_ticker = str(a[99]).split(">")[1].split("<")[0]
    fourth = str(span[160]).split(">")[1].split("<")[0]
    fourth_price = str(span[161]).split(">")[1].split("<")[0]
    fourth_change = str(span[163]).split(">")[1].split("<")[0]
    fourth_per_change = str(span[165]).split(">")[1].split("<")[0]

    fifth_ticker = str(a[100]).split(">")[1].split("<")[0]
    fifth = str(span[166]).split(">")[1].split("<")[0]
    fifth_price = str(span[167]).split(">")[1].split("<")[0]
    fifth_change = str(span[169]).split(">")[1].split("<")[0]
    fifth_per_change = str(span[171]).split(">")[1].split("<")[0]

    sixth_ticker = str(a[101]).split(">")[1].split("<")[0]
    sixth = str(span[172]).split(">")[1].split("<")[0]
    sixth_price = str(span[173]).split(">")[1].split("<")[0]
    sixth_change = str(span[175]).split(">")[1].split("<")[0]
    sixth_per_change = str(span[177]).split(">")[1].split("<")[0]

    seven_ticker = str(a[102]).split(">")[1].split("<")[0]
    seven = str(span[178]).split(">")[1].split("<")[0]
    seven_price = str(span[179]).split(">")[1].split("<")[0]
    seven_change = str(span[181]).split(">")[1].split("<")[0]
    seven_per_change = str(span[183]).split(">")[1].split("<")[0]

    eight_ticker = str(a[103]).split(">")[1].split("<")[0]
    eight = str(span[184]).split(">")[1].split("<")[0]
    eight_price = str(span[185]).split(">")[1].split("<")[0]
    eight_change = str(span[187]).split(">")[1].split("<")[0]
    eight_per_change = str(span[189]).split(">")[1].split("<")[0]

    nine_ticker = str(a[104]).split(">")[1].split("<")[0]
    nine = str(span[190]).split(">")[1].split("<")[0]
    nine_price = str(span[191]).split(">")[1].split("<")[0]
    nine_change = str(span[193]).split(">")[1].split("<")[0]
    nine_per_change = str(span[195]).split(">")[1].split("<")[0]

    ten_ticker = str(a[105]).split(">")[1].split("<")[0]
    ten = str(span[196]).split(">")[1].split("<")[0]
    ten_price = str(span[197]).split(">")[1].split("<")[0]
    ten_change = str(span[199]).split(">")[1].split("<")[0]
    ten_per_change = str(span[201]).split(">")[1].split("<")[0]

    table_date = [
        ['Ticker', 'Company', 'Price', 'Change', '% Change'],
        [first_ticker, first, first_price, first_change, first_per_change],
        [second_ticker, second, second_price, second_change, second_per_change],
        [third_ticker, third, third_price, third_change, third_per_change],
        [fourth_ticker, fourth, fourth_price, fourth_change, fourth_per_change],
        [fifth_ticker, fifth, fifth_price, fifth_change, fifth_per_change],
        [sixth_ticker, sixth, sixth_price, sixth_change, sixth_per_change],
        [seven_ticker, seven, seven_price, seven_change, seven_per_change],
        [eight_ticker, eight, eight_price, eight_change, eight_per_change],
        [nine_ticker, nine, nine_price, nine_change, nine_per_change],
        [ten_ticker, ten, ten_price, ten_change, ten_per_change]
    ]
    table = AsciiTable(table_date)
    print(table.table)

def sectors():
    url = "https://markets.money.cnn.com/Marketsdata/Sectors/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    a = soup.find_all('a')

    one_sector = str(a[84]).split(">")[1].split("<")[0]
    one_change = str(a[84]).split(">")[2].split("<")[0]

    two_sector = str(a[85]).split(">")[1].split("<")[0]
    two_change = str(a[85]).split(">")[2].split("<")[0]

    three_sector = str(a[86]).split(">")[1].split("<")[0]
    three_change = str(a[86]).split(">")[2].split("<")[0]

    four_sector = str(a[87]).split(">")[1].split("<")[0]
    four_change = str(a[87]).split(">")[2].split("<")[0]

    five_sector = str(a[88]).split(">")[1].split("<")[0]
    five_change = str(a[88]).split(">")[2].split("<")[0]

    six_sector = str(a[89]).split(">")[1].split("<")[0]
    six_change = str(a[89]).split(">")[2].split("<")[0]
    
    seven_sector = str(a[90]).split(">")[1].split("<")[0]
    seven_change = str(a[90]).split(">")[2].split("<")[0]

    eight_sector = str(a[91]).split(">")[1].split("<")[0]
    eight_change = str(a[91]).split(">")[2].split("<")[0]

    nine_sector = str(a[92]).split(">")[1].split("<")[0]
    nine_change = str(a[92]).split(">")[2].split("<")[0]

    ten_sector = str(a[93]).split(">")[1].split("<")[0]
    ten_change = str(a[93]).split(">")[2].split("<")[0]

    eleven_sector = str(a[94]).split(">")[1].split("<")[0]
    eleven_change = str(a[94]).split(">")[2].split("<")[0]

    table_date = [
        ['Industry', 'Change'],
        [one_sector, one_change],
        [two_sector, two_change],
        [three_sector, three_change],
        [four_sector, four_change],
        [five_sector, five_change],
        [six_sector, six_change],
        [seven_sector, seven_change],
        [eight_sector, eight_change],
        [nine_sector, nine_change],
        [ten_sector, ten_change],
        [eleven_sector, eleven_change]
    ]
    table = AsciiTable(table_date)
    print(table.table)

def key_stats():
    url = "https://money.cnn.com/data/markets/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.find_all('span')

    year_yield = str(span[42]).split(">")[1].split("<")[0]
    year_yield_per = str(span[43]).split(">")[4].split("<")[0] + str(span[43]).split(">")[6].split("<")[0]
    year_yield_change = str(span[45]).split(">")[1].split("<")[0] + str(span[46]).split(">")[1].split("<")[0]

    oil = str(span[49]).split(">")[1].split("<")[0]
    oil_price = str(span[51]).split(">")[1].split("<")[0] + str(span[52]).split(">")[1].split("<")[0]
    oil_change = str(span[55]).split(">")[1].split("<")[0] + "%"

    yen = str(span[56]).split(">")[1].split("<")[0]
    yen_price = str(span[58]).split(">")[1].split("<")[0] + str(span[59]).split(">")[1].split("<")[0]
    yen_change = str(span[62]).split(">")[1].split("<")[0] +"%"

    euro = str(span[63]).split(">")[1].split("<")[0]
    euro_price = str(span[65]).split(">")[1].split("<")[0] + str(span[66]).split(">")[1].split("<")[0]
    euro_change = str(span[69]).split(">")[1].split("<")[0] +"%"

    gold = str(span[70]).split(">")[1].split("<")[0]
    gold_price = str(span[72]).split(">")[1].split("<")[0] + str(span[73]).split(">")[1].split("<")[0]
    gold_change = str(span[76]).split(">")[1].split("<")[0] +"%"

    table_date = [
        ['Indicator', 'Value', 'Change'],
        [year_yield, year_yield_per, year_yield_change],
        [oil, oil_price, oil_change],
        [yen, yen_price, yen_change],
        [euro, euro_price, euro_change],
        [gold, gold_price, gold_change]
    ]
    table = AsciiTable(table_date)
    print(table.table)
