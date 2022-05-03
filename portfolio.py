from dotenv import load_dotenv
import os
from web3 import Web3
import eth_keys
from eth_account import account
from web3.middleware import geth_poa_middleware
import json
import pandas as pd
import requests
import numpy as np
import datetime

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
    return result

def view_trades_polygon(address):
    w3 = Web3(Web3.HTTPProvider(f'{INFURA_URL}/{INFURA_PROJECT_ID}'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    covey_ledger = w3.eth.contract(address = COVEY_LEDGER_POLYGON_ADDRESS, abi = ledger_info['abi'])
    my_address = w3.toChecksumAddress(address)
    result = covey_ledger.functions.getAnalystContent(my_address).call()
  # output format [('address', 'position string', unix time),('address', 'position string', unix time),...]
    return result

def calculate_portfolio(address,startCash):

    trades = view_trades_skale(address)
    
    tradingKey = pd.DataFrame(columns=["id", "entry_price", "entry_date", "market_entry_date", "symbol", "percent", "current_position", 
    "split_adjusted_entry", "prior_portfolio_value", "target_position_value", "prior_position_value", "cash_used", 
    "share_count", "prior_cumulative_share_count", "post_cumulative_share_count", "status", 
    "address", "realized_profit"])
    
    '''FILL IN tradingKey here from trades'''

    prices = pd.read_csv('prices.csv')

    portfolio = pd.DataFrame(columns=["date_time", "address", "cash", "usd_value", 
                                      "inception_return"])

    firstRow = {"date_time": firstTrade, "address": address, "cash": startCash, "usd_value": startCash, 
                "inception_return": 1.0}
    
    ''' CALCULATE PORTFOLIO HERE from tradingKey and prices '''
    
    return tradingKey, prices, portfolio

def createTickerTable(address): 
  tradingKey = pd.DataFrame(columns=["id", "entry_price", "entry_date", "market_entry_date", "symbol", "percent", "current_position", 
    "split_adjusted_entry", "prior_portfolio_value", "target_position_value", "prior_position_value", "cash_used", 
    "share_count", "prior_cumulative_share_count", "post_cumulative_share_count", "status", 
    "address", "realized_profit"])

  trade_ledger = pd.DataFrame({'symbol':[], 'size':[], 'date_time':[], 'date_time_utc':[]})
  trades = view_trades_skale(address) 
  portfolio_num = 1
  for i in range(len(trades)):
      length_temp = len(trades[i][1].split(','))
      daily_trade_ledger = pd.DataFrame({'symbol':[None]*length_temp, 'size':[None]*length_temp, 'date_time':[None]*length_temp})    
      for j in range(len(trades[i][1].split(','))):
          daily_trade_ledger.iloc[j,0] = trades[i][1].split(',')[j].split(':')[0]        
          daily_trade_ledger.iloc[j,1]  = trades[i][1].split(',')[j].split(':')[1]
          daily_trade_ledger.iloc[j,2]  = trades[i][2]
      trade_ledger = pd.concat([trade_ledger, daily_trade_ledger ])
  trade_ledger.rename(columns= {'date_time': 'date_time_unix'}, inplace=True)    
  trade_ledger.date_time_utc = [datetime.datetime.fromtimestamp(i) for i in trade_ledger.date_time_unix]
  
  trade_ledger.date_time_utc = pd.to_datetime(trade_ledger.date_time_utc, utc=True)
  trade_ledger.Size = pd.to_numeric(trade_ledger.size)
  # we round up our time to prevent look ahead bias
  trade_ledger['date_time_utc_full_hour'] = trade_ledger['date_time_utc'].dt.ceil('60min')
  trade_ledger.to_csv(f'trade_ledger_{portfolio_num}.csv')
  
  return trade_ledger

# user_id 30
#OLD: 
createTickerTable('0x7508438ff36b72fc07b044b6a88fd57dbe4cf633').to_csv('tradingKeyOldSwingAdj.csv')
#NEW: 
createTickerTable('0x0d97A0E7e42eB70d013a2a94179cEa0E815dAE41').to_csv('tradingKeyNewSwingAdj.csv')
#print(view_trades_skale('0xaa7f0957a2ea0c07f75950bb8006240480a9d913') )
# Address Two 
#view_trades_skale('0x211fe601e24ce89cb443356f687c67fbf7708412')
# Price Pull
#print(pd.read_csv('prices.csv'))

