import pyupbit

# 원화 거래 가능 코인 리스트
ticker_list = pyupbit.get_tickers(fiat="KRW")

# 목표가 계산 함수
def calc_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day", 2)
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return target

# 변동성 돌파 계수 계산 함수
def calc_coefficient(ticker):
    current_price = pyupbit.get_current_price(ticker)
    coefficient = current_price - calc_target(ticker)
    return coefficient