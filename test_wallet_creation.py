#!/usr/bin/env python3
"""
Day-2 demo: generate and store encrypted EVM + Solana wallets,
then print public addresses.
"""

import os
from dotenv import load_dotenv
from wallet_store_sql import WalletStore

# Load env vars
load_dotenv()

MASTER_KEY = os.getenv("MASTER_KEY")
if not MASTER_KEY:
    raise EnvironmentError("MASTER_KEY not set in .env")

def main():
    store = WalletStore(db_path="wallets.db", master_key=MASTER_KEY)
    user_id = "test_user"
    evm_addr, sol_addr = store.create_wallets_for_user(user_id)
    print(f"Created wallets for user: {user_id}")
    print(f"EVM Address: {evm_addr}")
    print(f"Solana Address: {sol_addr}")

if __name__ == "__main__":
    main()
