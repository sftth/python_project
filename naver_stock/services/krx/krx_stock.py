from pykrx import stock
import pandas as pd
import datetime

def fetch_krx_ticker_list(market='KOSPI'):
    print(f"Start krx ticker list")
    ticker_list = stock.get_market_ticker_list(market=market.upper())

    # 리스트를 데이터프레임으로 변환
    df = pd.DataFrame(ticker_list, columns=[market.upper()])

    print(df)
    print(f"Finish krx ticker list")
    return df

def fetch_krx_stock_price_by_ticker(from_date, to_date, ticker):
    print(f"{from_date} {to_date} target ticker: {ticker}")

    df = stock.get_market_ohlcv(from_date, to_date, ticker)

    return df

def fetch_krx_stock_price_monthly(from_date, to_date, ticker ):
    print(f"{from_date} {to_date} target ticker: {ticker}")

    df = stock.get_market_ohlcv(from_date, to_date, ticker, 'm')

    return df

def fetch_krx_stock_fundamental(date, market='KOSPI'):
    print(f"Start {date}-{market}-fundamental")

    # 전체 데이터 불러오기
    pd.set_option('display.max_columns', None)
    df = stock.get_market_fundamental_by_ticker(date, market)

    print(df.head(3))

    # 인덱스(티커)를 컬럼으로 변환
    df.reset_index(inplace=True)

    return df

def fetch_krx_stock_fundamental_by_ticker(from_date, to_date, ticker):
    print(f"Start {from_date}-{to_date}-{ticker}-fundamental")
    df = stock.get_market_fundamental(from_date, to_date, ticker)

    print(df.head(3))

    return df

def fetch_krx_per_top10(market='KOSPI'):
    today = datetime.datetime.today().strftime('%Y%m%d')
    pd.set_option('display.max_columns', None)
#    df = stock.get_market_fundamental_by_ticker(today, market=market.upper())
    df = stock.get_market_fundamental('20250418')

    print(df)

    # PER 값이 있는 데이터만 필터링
#    df = df[df['PER'].notna()]

    # PER 기준 오름차순 정렬 후 상위 10개 선택
#    top10 = df.sort_values(by='PER').head(10)

#    return top10

def save_to_excel(df,market, filename="per_top10_kospi"):
    try:
        output_filename = f"{filename}_{market}.xlsx"
        df.to_excel(output_filename, index=False)

        print(f"저장 완료: {filename}")
    except Exception as e:
        print(f"엑셀 저장 중 오류 발생: {e}")