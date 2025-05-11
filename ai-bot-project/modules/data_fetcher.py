import yfinance as yf
import json

def fetch_data(symbol, period="1mo", interval="1h"):
    return yf.download(symbol, period=period, interval=interval)

def load_config():
    with open("configs/config.json") as f:
        return json.load(f)