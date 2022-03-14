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

# Environment Variables you will need

Create a file called `.env` and add the following variables:

-   WALLET_PRIVATE_KEY
-   INFURA_PROJECT_ID
-   COVEY_LEDGER_ADDRESS (for polygon testnet the address is `0xAd995FBA14dC6A369faE3c90B81CE0346f4Cf3BC`)
-   WALLET (this is the address of your wallet, it is the private key above)
-   POLYGON_CHAIN_ID (for the polygon testnet it is `80001`)

