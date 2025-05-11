# bot.py
import yfinance as yf
import pandas_ta as ta

def get_signals(symbol="^NSEI"):
    data = yf.download(symbol, period="1mo", interval="1h")
    data['SMA_20'] = ta.sma(data['Close'], 20)
    data['SMA_50'] = ta.sma(data['Close'], 50)
    data['Signal'] = (data['SMA_20'] > data['SMA_50']).astype(int)
    return data
# Add this function
def backtest(data):
    data['Return'] = data['Close'].pct_change()
    data['Strategy'] = data['Signal'].shift(1) * data['Return']
    return data[['Return', 'Strategy']].cumsum().plot()
if __name__ == "__main__":
    print(get_signals().tail())
