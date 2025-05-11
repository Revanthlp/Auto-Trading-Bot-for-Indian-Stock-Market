# bot.py
import yfinance as yf
import pandas_ta as ta

def get_signals(symbol="^NSEI"):
    data = yf.download(symbol, period="1mo", interval="1h")
    data['SMA_20'] = ta.sma(data['Close'], 20)
    data['SMA_50'] = ta.sma(data['Close'], 50)
    data['Signal'] = (data['SMA_20'] > data['SMA_50']).astype(int)
    return data

if __name__ == "__main__":
    print(get_signals().tail())
