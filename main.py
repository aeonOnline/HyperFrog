from wallet_utils import get_balance_with_usd

if __name__ == "__main__":
    eth_balance, usd_value = get_balance_with_usd()
    print(f"ETH Balance: {eth_balance} ETH")
    print(f"USD Value (mock): ${usd_value}")
