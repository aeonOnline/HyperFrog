from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

if not RPC_URL or not WALLET_ADDRESS:
    raise ValueError("RPC_URL and WALLET_ADDRESS must be set in .env")

web3 = Web3(Web3.HTTPProvider(RPC_URL))

def get_eth_balance():
    """Fetch ETH balance in Ether units."""
    balance_wei = web3.eth.get_balance(WALLET_ADDRESS)
    balance_eth = web3.from_wei(balance_wei, "ether")
    return balance_eth

def get_balance_with_usd():
    """Return ETH balance and mocked USD equivalent."""
    eth_balance = get_eth_balance()
    usd_price = 4444  # Mock price
    return eth_balance, eth_balance * usd_price
