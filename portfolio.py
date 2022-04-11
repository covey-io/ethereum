from dotenv import load_dotenv
import os
from web3 import Web3
import eth_keys
from eth_account import account
from web3.middleware import geth_poa_middleware
import json
import pandas as pd
import requests

load_dotenv()

WALLET = os.getenv('WALLET')
INFURA_PROJECT_ID = os.getenv('INFURA_PROJECT_ID')
INFURA_URL = os.getenv('INFURA_URL')
POLYGON_CHAIN_ID= os.getenv('POLYGON_CHAIN_ID')
COVEY_LEDGER_POLYGON_ADDRESS = os.getenv('COVEY_LEDGER_POLYGON_ADDRESS')

COVEY_LEDGER_SKALE_ADDRESS = os.getenv('COVEY_LEDGER_SKALE_ADDRESS')
SKALE_URL = os.getenv('SKALE_URL')

IEX_TOKEN = os.getenv('IEX_TOKEN')

# Opening JSON file
f = open('CoveyLedger.json')
 
# returns JSON object as
# a dictionary
ledger_info = json.load(f)


def view_trades_skale(address):
    w3 = Web3(Web3.HTTPProvider(SKALE_URL))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    covey_ledger = w3.eth.contract(address = COVEY_LEDGER_SKALE_ADDRESS, abi = ledger_info['abi'])
    my_address = w3.toChecksumAddress(address)
    result = covey_ledger.functions.getAnalystContent(my_address).call()
  # output format [('address', 'position string', unix time),('address', 'position string', unix time),...]
    print(result)

def view_trades_polygon(address):
    w3 = Web3(Web3.HTTPProvider(f'{INFURA_URL}/{INFURA_PROJECT_ID}'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    covey_ledger = w3.eth.contract(address = COVEY_LEDGER_POLYGON_ADDRESS, abi = ledger_info['abi'])
    my_address = w3.toChecksumAddress(address)
    result = covey_ledger.functions.getAnalystContent(my_address).call()
  # output format [('address', 'position string', unix time),('address', 'position string', unix time),...]
    print(result)


def get_prices(symbols,exactDate):   
    #docs:  '''https://iexcloud.io/docs/api/#historical-prices'''
    root_url = 'https://cloud.iexapis.com/stable/stock/market/batch?symbols='
    method = '&types=intraday-prices&'
    exactDate = pd.to_datetime(exactDate,infer_datetime_format=True)
    exactDate = exactDate.strftime('%Y%m%d')
    quotes = dict()
    for xOf100 in range(0,len(symbols),100) : 
        urlVersion = symbols[xOf100:xOf100+100]
        urlVersion = ",".join(urlVersion)
        url = root_url+urlVersion+method+'&token='+IEX_TOKEN+'&exactDate='+exactDate
        data = json.loads(requests.get(url).text)
        quotes.update(data)
    print(quotes)
    return quotes 


def calculate_portfolio(address,startCash):

    trades = view_trades_skale(address)
    
    tradingKey = pd.DataFrame(columns=["id", "entry_price", "entry_date", "market_entry_date", "symbol", "percent", "current_position", 
    "adjusted_entry", "prior_portfolio_value", "target_position_value", "prior_position_value", "cash_used", 
    "share_count", "prior_cumulative_share_count", "post_cumulative_share_count", "status", "posted_on_chain", 
    "address", "realized_profit", "exchange", "delayed_trade_date", "currency"]
    
    ''' FILL IN tradingKey here from trades'''

    prices = pd.DataFrame(columns=["id", "date_time", "price", "symbol"]

    ''' FILL in prices here from tradingKey '''

    portfolio = pd.DataFrame(columns=["date_time", "address", "cash", "usd_value", 
                                      "inception_return"])

    firstRow = {"date_time": firstTrade, "address": address, "cash": startCash, "usd_value": startCash, 
                "inception_return": 1.0}
    
    ''' CALCULATE PORTFOLIO HERE from tradingKey and prices '''
    
    return tradkingKey, prices, portfolio

# Address One 
#view_trades_skale('0x41da2035ac26e4308b624a84d3caebf80a4dccf1') 
# Address Two 
#view_trades_skale('0x211fe601e24ce89cb443356f687c67fbf7708412')
# Price Pull
#get_prices(['FB','GOOGL'],'2022-03-29')
