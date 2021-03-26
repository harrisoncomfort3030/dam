import pandas as pd
import numpy as np
import time
import requests as r
import json


#coins that are in the website header
header_coins_string = 'bitcoin,ethereum,polkadot,kusama,havven,sushi'
header_coins_symbol_dict = {
    "bitcoin": 'BTC',
    "ethereum": 'ETH',
    "polkadot": 'DOT',
    "kusama": 'KSM',
    "havven": 'SNX',
    "sushi": 'SUSHI'

}

#coins that are in the portfolio
portfolio_coins_string = 'renbtc,ethereum,havven,sushi,ocean-protocol,republic-protocol,sora,axie-infinity'
portfolio_coins_symbol_dict = {
"renbtc": 'renBTC',
"havven": 'SNX',
"sushi": 'SUSHI',
"ethereum": 'ETH',
"ocean-protocol": 'OCEAN',
"republic-protocol": 'REN',
"sora": 'XOR',
"axie-infinity": 'AXS',
}


#get price and 24-hour performance data on specific coins
def get_coin_info(coins_string): #coins as a string
    coin_info_api = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd&include_24hr_change=true".format(coins_string)
    coin_info_string = r.get(coin_info_api).content.decode()
    coin_info_json = json.loads(coin_info_string)
    return coin_info_json

#create dictionary with right symbol, price and 24 hour percent change
def get_website_header_coin_info (dict):
    website_header_coins_data = []
    for coin in dict.items():
        symbol = header_coins_symbol_dict[coin[0]]
        price_raw = float(round((coin[1]['usd']),1))
        price = "{:,}".format(price_raw)
        usd_change = str(round(coin[1]['usd_24h_change'],2))+"%"

        coin_info_dict = {
        'symbol': symbol,
        'price': price,
        '24_hour_change': usd_change
        }
        website_header_coins_data.append(coin_info_dict)

    return website_header_coins_data

#get performance data for portfolio coins
def get_portfolio_coin_info (dict):
    portfolio_coins_data = []
    for coin in dict.items():
        symbol = portfolio_coins_symbol_dict[coin[0]]
        usd_change = str(round(coin[1]['usd_24h_change'],1))+"%"
        coin_info_dict = {
        symbol: usd_change
        }
        portfolio_coins_data.append(coin_info_dict)

    return portfolio_coins_data


def main():
    website_header_coin_info_dict = get_coin_info(header_coins_string)
    website_header_coins_data_list = get_website_header_coin_info(website_header_coin_info_dict)
    print(website_header_coins_data_list)
    portfolio_coin_info_dict = get_coin_info(portfolio_coins_string)
    portfolio_coins_data_list = get_portfolio_coin_info(portfolio_coin_info_dict)
    print(portfolio_coins_data_list)

main()
