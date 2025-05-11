import argparse
from datetime import datetime
from modules.data_fetcher import fetch_data, load_config
from modules.strategy import generate_signals
from modules.backtester import backtest
from modules.telegram_notifier import TelegramNotifier
import os

def main():
    # Configuration
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="^NSEI")
    args = parser.parse_args()
    
    config = load_config()
    
    # Core Logic
    data = fetch_data(args.symbol, interval=config["timeframe"])
    signals = generate_signals(data, config["sma_short"], config["sma_long"])
    
    # Backtest and Save Results
    plot_path = f"outputs/backtest_results/{datetime.now().strftime('%Y%m%d')}.png"
    backtest(signals, plot_path)
    
    # Generate Signal
    last_signal = "BUY" if signals['Signal'].iloc[-1] == 1 else "SELL"
    price = signals['Close'].iloc[-1]
    
    # Telegram Alert
    message = (
        f"<b>{args.symbol} Signal</b>\n"
        f"🟢 {last_signal} at {price:.2f}\n"
        f"📊 SMA{config['sma_short']}/{config['sma_long']} Crossover\n"
        f"⏰ {datetime.now().strftime('%d %b %Y %H:%M')}"
    )
    
    notifier = TelegramNotifier()
    notifier.send_alert(message, plot_path)

if __name__ == "__main__":
    main()