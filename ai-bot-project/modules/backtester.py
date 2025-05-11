import matplotlib.pyplot as plt

def backtest(data, save_path=None):
    data['Return'] = data['Close'].pct_change()
    data['Strategy'] = data['Signal'].shift(1) * data['Return']
    
    plt.figure(figsize=(12,6))
    plt.title("Backtest Results - SMA Crossover Strategy")
    data[['Return','Strategy']].cumsum().plot()
    plt.ylabel("Cumulative Returns")
    plt.grid(True)
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()