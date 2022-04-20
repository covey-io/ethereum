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

def calculate_portfolio(address,startCash):

    trades = view_trades_skale(address)
    
    tradingKey = pd.DataFrame(columns=["id", "entry_price", "entry_date", "market_entry_date", "symbol", "percent", "current_position", 
    "adjusted_entry", "prior_portfolio_value", "target_position_value", "prior_position_value", "cash_used", 
    "share_count", "prior_cumulative_share_count", "post_cumulative_share_count", "status", "posted_on_chain", 
    "address", "realized_profit", "exchange", "delayed_trade_date", "currency"])
    
    '''FILL IN tradingKey here from trades'''

    prices = pd.read_csv('prices.csv')

    portfolio = pd.DataFrame(columns=["date_time", "address", "cash", "usd_value", 
                                      "inception_return"])

    firstRow = {"date_time": firstTrade, "address": address, "cash": startCash, "usd_value": startCash, 
                "inception_return": 1.0}
    
    ''' CALCULATE PORTFOLIO HERE from tradingKey and prices '''
    
    return tradingKey, prices, portfolio

# Address One 
#view_trades_skale('0x41da2035ac26e4308b624a84d3caebf80a4dccf1') 
# Address Two 
#view_trades_skale('0x211fe601e24ce89cb443356f687c67fbf7708412')
# Price Pull
#print(pd.read_csv('prices.csv'))

