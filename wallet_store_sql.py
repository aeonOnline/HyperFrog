#!/usr/bin/env python3
import os
import sqlite3
from cryptography.fernet import Fernet
from web3 import Account
from solders.keypair import Keypair
import base58

class WalletStore:
    def __init__(self, db_path="wallets.db", master_key=None):
        self.db_path = db_path
        if not master_key:
            raise ValueError("MASTER_KEY is required for encryption")
        self.fernet = Fernet(master_key)
        self.conn = sqlite3.connect(self.db_path)
        self._init_db()

    def _init_db(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS wallets (
                user_id TEXT PRIMARY KEY,
                evm_address TEXT,
                evm_priv_encrypted TEXT,
                sol_address TEXT,
                sol_priv_encrypted TEXT
            )
        """)
        self.conn.commit()

    def create_evm_wallet(self, user_id):
        acct = Account.create()
        encrypted_priv = self.fernet.encrypt(acct.key)
        self.conn.execute("""
            INSERT OR REPLACE INTO wallets (user_id, evm_address, evm_priv_encrypted)
            VALUES (?, ?, ?)
        """, (user_id, acct.address, encrypted_priv))
        self.conn.commit()
        return acct.address

    def create_solana_wallet(self, user_id):
        keypair = Keypair()
        pubkey = str(keypair.pubkey())
        privkey_bytes = bytes(keypair)
        privkey_b58 = base58.b58encode(privkey_bytes)
        encrypted_priv = self.fernet.encrypt(privkey_b58)
        self.conn.execute("""
            UPDATE wallets SET sol_address=?, sol_priv_encrypted=?
            WHERE user_id=?
        """, (pubkey, encrypted_priv, user_id))
        self.conn.commit()
        return pubkey

    def create_wallets_for_user(self, user_id):
        evm_address = self.create_evm_wallet(user_id)
        sol_address = self.create_solana_wallet(user_id)
        return evm_address, sol_address
