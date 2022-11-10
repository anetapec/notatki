def calc_location(start_capital,percentage,time):
    value = start_capital * (1 + percentage / 100) ** time
    return value

