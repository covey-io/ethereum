from dotenv import load_dotenv
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
 


load_dotenv()

WALLET = os.getenv('WALLET')
WALLET_PRIVATE_KEY = os.getenv('WALLET_PRIVATE_KEY')
INFURA_PROJECT_ID = os.getenv('INFURA_PROJECT_ID')
COVEY_LEDGER_ADDRESS = os.getenv('COVEY_LEDGER_ADDRESS')
POLYGON_CHAIN_ID= os.getenv('POLYGON_CHAIN_ID')

# Opening JSON file
f = open('CoveyLedger.json')
 
# returns JSON object as
# a dictionary
ledger_info = json.load(f)

# You can switch this to polygon "mainnet" by using matic.infura instead of mumbai
w3 = Web3(Web3.HTTPProvider(f'https://polygon-mumbai.infura.io/v3/{INFURA_PROJECT_ID}'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def post_trades(tradeString):
  covey_ledger = w3.eth.contract(address = COVEY_LEDGER_ADDRESS, abi = ledger_info['abi'])
  nonce = w3.eth.get_transaction_count(WALLET)

  txn = covey_ledger.functions.createContent(tradeString).buildTransaction({
    'chainId': int(POLYGON_CHAIN_ID),
    'gas': 15000000,
    'nonce': nonce,
  })
  signed_txn = w3.eth.account.sign_transaction(txn, private_key=WALLET_PRIVATE_KEY)
  w3.eth.send_raw_transaction(signed_txn.rawTransaction)  

def view_trades(address):
  covey_ledger = w3.eth.contract(address = COVEY_LEDGER_ADDRESS, abi = ledger_info['abi'])

  result = covey_ledger.functions.getAnalystContent(address).call()
  print(result)

#post_trades('XRPUSDT:0.2')
view_trades(WALLET)