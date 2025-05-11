import pandas_ta as ta

def generate_signals(data, short=20, long=50):
    data['SMA_20'] = ta.sma(data['Close'], short)
    data['SMA_50'] = ta.sma(data['Close'], long)
    data['Signal'] = (data['SMA_20'] > data['SMA_50']).astype(int)
    return data