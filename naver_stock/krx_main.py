from naver_stock.services.krx.krx_stock import save_to_excel, fetch_krx_stock_price_monthly
from naver_stock.services.krx.krx_stock import fetch_krx_per_top10
from naver_stock.services.krx.krx_stock import fetch_krx_ticker_list
from naver_stock.services.krx.krx_stock import fetch_krx_stock_price_by_ticker
from naver_stock.services.krx.krx_stock import fetch_krx_stock_fundamental
from naver_stock.services.krx.krx_stock import fetch_krx_stock_fundamental_by_ticker
from datetime import datetime

if __name__ == '__main__':
    # ticker lists per market
    market_list = ['KOSPI', 'KOSDAQ']
    today_str = datetime.today().strftime("%Y%m%d")
#    for item in market_list:
#        ticker_list = fetch_krx_ticker_list(market=item)
#        save_to_excel(ticker_list, market=item, filename="ticker_list")
    # stock price per ticker
#    stock_price = fetch_krx_stock_price_by_ticker('20250401', '20250418', '095570')
#    save_to_excel(stock_price, market='KOSPI', filename='095570')

    # Fundamental
    for item in market_list:
        fundamental = fetch_krx_stock_fundamental(date=today_str, market=item)
        save_to_excel(fundamental, market=item, filename='fundamental')


#    top10_per = fetch_krx_per_top10()
#    save_to_excel(top10_per)