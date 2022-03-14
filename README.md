# Covey-ethereum

The purpose of this project is to show how to send transactions to ethereum like networks, in this case POLYGON

# Requirements

-   [Infura Node](https://infura.io/) with the polygon add-on enabled.
-   A wallet with some MATIC to transact. For testing, can use this [faucet](https://faucet.polygon.technology/). 
-    For mainnet buy MATIC on an exchange, 100 trades is $0.25 worth of Matic 
-   The wallet's private key and address

# Setup

-   Run `pip install`
-   Create virtual env  `python3 -m venv env`
-   Activate virtual env `source env/bin/activate`
-   Should get an (env) in terminal 
-   Then `pip install -r requirements.txt`
-   Then in the command line `python main.py`

# Polygon Mainnet Environment Variables (pick either MAINNET or TESTNET)

Create a file called `.env` and add the following variables:
WALLET = ''
WALLET_PRIVATE_KEY = ''
INFURA_PROJECT_ID = ''

INFURA_URL = 'https://polygon-mainnet.infura.io/v3'
COVEY_LEDGER_ADDRESS = '0x587Ec5a7a3F2DE881B15776BC7aaD97AA44862Be' 
POLYGON_CHAIN_ID = 137

# Polygon Testnet Environment Variables (pick either MAINNET or TESTNET)

Create a file called `.env` and add the following variables:
WALLET = ''
WALLET_PRIVATE_KEY = ''
INFURA_PROJECT_ID = ''

INFURA_URL = 'https://polygon-mumbai.infura.io/v3'
COVEY_LEDGER_ADDRESS = '0xAd995FBA14dC6A369faE3c90B81CE0346f4Cf3BC' 
POLYGON_CHAIN_ID = 80001
