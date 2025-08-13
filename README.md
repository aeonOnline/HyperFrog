# HyperFrog 🐸

**HyperFrog** is an open-source public-goods project for the [Hyperliquid Hackathon](https://hyperliquid.xyz/).
It combines a Telegram bot and a background "yield engine" to automate swaps and yield strategies on **HyperEVM**.

---

## 📅 Progress
- **Day 1:** Project scaffolded with basic wallet store and encryption.
- **Day 2:** Added runnable wallet generation demo + `.env.example`.
## Day 3: Fetch Wallet Balance
- Added `wallet_utils.py` with functions to get ETH balance and mock USD conversion.
- Uses `web3.py` to connect to RPC.
- Updated `.env.example` with `RPC_URL` and `WALLET_ADDRESS`.
- Now running `python main.py` will print the wallet's balance in ETH and USD.
---

## 🛠 Setup

### 1. Clone the repository
```bash
git clone https://github.com/aeonOnline/HyperFrog.git
cd HyperFrog
