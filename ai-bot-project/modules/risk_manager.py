def calculate_position_size(capital, risk_pct, stop_loss):
    return (capital * risk_pct) / abs(stop_loss)