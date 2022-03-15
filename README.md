# Covey-ethereum

The purpose of this project is to show how to send transactions to ethereum like networks, in this case POLYGON

# Requirements

-   [Infura Node](https://infura.io/) with the polygon add-on enabled.
-   A wallet with some MATIC to transact. For testing, can use this [faucet](https://faucet.polygon.technology/).
-   For mainnet buy MATIC on an exchange, 100 trades is $0.25 worth of Matic
-   The wallet's private key and address

# Setup

-   Run `pip install`
-   Create virtual env `python3 -m venv env`
-   Activate virtual env `source env/bin/activate`
-   Should get an (env) in terminal
-   Then `pip install -r requirements.txt`
-   Then in the command line `python main.py`

# Polygon Mainnet Environment Variables (pick either MAINNxT or TESTNET)

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

# Generating accounts for use with this repo

-   Install [geth](https://geth.ethereum.org/)
-   Run geth in your command line by using the command `geth` [More info here](https://geth.ethereum.org/docs/interface/command-line-options)
-   Run the Javascript console by running `geth console` on windows I recommend `geth attach ipc:\\.\pipe\geth.ipc`
-   Load the account generation script by running `loadScript("./accountGenerator.js")` while inside this directory in the command line
-   Now run `generateAccounts` with the desired number of accounts and a password. So if you want to generate 50 accounts with the password of "password" do `generateNewAccounts("password",50)`
-   It will print the address of the accounts. I would copy and save this in a text file
-   Alternatively you can run `geth account list` in the command line
-   In `main.py` you can use `get_private_keys` to list all the private keys for all your accounts
-   Alternatively you can use `get_private_key` to list the private key for a given address
-   Once you choose a private key and an address, set these to the `WALLET` and `WALLET_PRIVATE_KEY` env vars or edit the code to use the given hardcoded values.
-   Make sure to give yor new account some MATIC using a [faucet](https://faucet.polygon.technology/)