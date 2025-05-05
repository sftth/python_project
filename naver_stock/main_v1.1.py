# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from naver_stock.services.ht_stock import ht_save_xlsx
from naver_stock.services.nh_stock import nh_save_xlsx
from naver_stock.services.mn_stock import mn_save_xlsx
from naver_stock.services.get_stock_details import get_stock_info, get_stock_info_v1

#NH투자증권
nh_stock_list = [
["domestic","stock","HPSP","403870"],
["domestic","etf","KODEX 미디어&엔터테인먼트","266360"],
["domestic","etf","KODEX 코스닥150레버리지","233740"],
["domestic","stock","LG생활건강","051900"],
["domestic","stock","LG씨엔에스","064400"],
["domestic","stock","LG전자","066570"],
["domestic","stock","LS에코에너지","229640"],
["domestic","stock","Plus 한화그룹주","0000J0"],
["domestic","stock","POSCO홀딩스","005490"],
["domestic","stock","SAMG엔터","419530"],
#["domestic","stock","SK하이닉스","000660"],
["domestic","stock","SOL 조선 TOP3플러스","466920"],
["domestic","etf","TIGER 200에너지화학레버리지","243890"],
["domestic","etf","TIGER 미국S&P500","360750"],
["domestic","etf","TIGER 미국나스닥100커버드콜(합성)","441680"],
["domestic","stock","대한항공","003490"],
["domestic","stock","두산에너빌리티","034020"],
["domestic","stock","디어유","376300"],
["domestic","stock","삼성전자","005930"],
["domestic","stock","삼성중공업","010140"],
["domestic","stock","세아제강","306200"],
["domestic","stock","솔트룩스","304100"],
["domestic","stock","쏠리드","050890"],
["domestic","stock","에코프로비엠","247540"],
["domestic","stock","오뚜기","007310"],
["domestic","stock","코오롱티슈진","950160"],
["domestic","stock","포스코인터내셔널","047050"],
["domestic","stock","포스코퓨처엠","003670"],
["domestic","stock","한국항공우주","047810"],
["domestic","stock","한샘","009240"],
#["domestic","stock","한화에어로스페이스","012450"],
#["domestic","stock","한화오션","042660"],
["domestic","stock","현대ADM","187660"],
["domestic","stock","현대로템","064350"],
["domestic","stock","현대지에프홀딩스","005440"],
["domestic","stock","현대차","005380"],
["domestic","stock","후성","093370"]
]
#한국투자증권
ht_stock_list = [
["domestic","stock","그래디언트","035080"],
["domestic","stock","대원미디어","048910"],
["domestic","stock","에스디바이오센서","137310"],
["domestic","stock","웅진씽크빅","095720"],
#["domestic","stock","카카오","035720"],
["domestic","stock","카카오게임즈","293490"],
["domestic","stock","카카오뱅크","323410"],
["domestic","stock","펄어비스","263750"],
["domestic","stock","LG에너지솔루션","373220"],
["domestic","stock","LG전자","066570"],
["domestic","stock","NAVER","035420"],
["domestic","stock","SK리츠","395400"],
#["domestic","stock","TIGER 차이나전기차SOLACTIVE","371460"],
#["domestic","stock","TIGER 차이나항셍테크","371160"],
["domestic","stock","TIGER배당커버드콜액티브","472150"],
["domestic","stock","TIGER은행고배당플러스 TOP10","466940"],
["worldstock","etf","YieldMax COIN Option Income Strategy ETF","CONY.K"],
["worldstock","etf","Volatility shares bitcoin strategy 2x ETF","BITX.K"]
]
#미니스탁
mn_stock_list = [
["worldstock","stock","애플","AAPL.O"],
["worldstock","stock","아마존","AMZN.O"],
["worldstock","stock","뱅크오브아메리카","BAC"],
["worldstock","stock","블랙록","BLK"],
["worldstock","stock","블랙스톤","BX"],
["worldstock","stock","코인베이스 글로벌","COIN.O"],
["worldstock","stock","세일즈포스닷컴","CRM"],
["worldstock","etf","SPDR 다우존스 ETF","DIA"],
["worldstock","stock","알파벳C주","GOOG.O"],
["worldstock","stock","골드만 삭스 그룹","GS"],
["worldstock","stock","아이온큐","IONQ.K"],
["worldstock","etf","아이셰어즈 코어 S&P500 ETF","IVV"],
["worldstock","etf","아이셰어즈 글로벌 금융 ETF","IXG"],
["worldstock","etf","JP모간 에쿼티 프리미엄 인컴 ETF","JEPI.K"],
["worldstock","stock","제이피모간 체이스","JPM"],
["worldstock","stock","코카콜라","KO"],
["worldstock","stock","메타 플랫폼스","META.O"],
["worldstock","stock","마이크로소프트","MSFT.O"],
["worldstock","stock","넷플릭스","NFLX.O"],
["worldstock","stock","엔비디아","NVDA.O"],
["worldstock","stock","리얼티 인컴","O"],
["worldstock","stock","유니버설 디스플레이","OLED.O"],
["worldstock","etf","아이셰어즈 우선주 ETF","PFF.O"],
["worldstock","stock","팔란티어 테크놀로지스 A주","PLTR.O"],
["worldstock","stock","펠로톤 인터렉티브","PTON.O"],
["worldstock","etf","인베스코 QQQ ETF","QQQ.O"],
["worldstock","etf","인베스코 나스닥100 ETF","QQQM.O"],
["worldstock","etf","글로벌엑스 나스닥 100 커버드콜 ETF","QYLD.O"],
["worldstock","etf","슈왑 미국 배당주 ETF","SCHD.K"],
["worldstock","stock","sea ADR","SE"],
["worldstock","stock","슈퍼 마이크로 컴퓨터","SMCI.O"],
["worldstock","stock","소파이 테크놀로지스","SOFI.O"],
["worldstock","etf","인베스코 S&P500 고배당 저변동성 ETF","SPHD.K"],
["worldstock","etf","인베스코 S&P500 저변동성 ETF","SPLV.K"],
["worldstock","etf","SPDR S&P500 ETF","SPY"],
["worldstock","etf","프로셰어즈 나스닥100 3배 레버리지 ETF","TQQQ.O"],
["worldstock","stock","테슬라","TSLA.O"],
["worldstock","stock","유나이티드 에어라인 홀딩스","UAL.O"],
["worldstock","stock","업스타트 홀딩스","UPST.O"],
["worldstock","etf","뱅가드 S&P500 ETF","VOO"],
["worldstock","etf","SPDR 미국 항공우주&방위산업 ETF","XAR"],
["worldstock","stock","블록","XYZ"]
]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("🔄 Starting save xlsx for ht...")
#    ht_save_xlsx()
    get_stock_info_v1(ht_stock_list, prefix="ht", output_dir="output/ht")
    print("✅ Save xlsx for ht completed.")

    print("🔄 Starting save xlsx for nh...")
#    nh_save_xlsx()
    get_stock_info_v1(nh_stock_list, prefix="nh", output_dir="output/nh")
    print("✅ Save xlsx for nh completed.")

    print("🔄 Starting save xlsx for mn...")
    get_stock_info_v1(mn_stock_list, prefix="mn", output_dir="output/mn")
#    mn_save_xlsx()
#    nh_save_stock_infos(mn_stock_list, prefix="mn_stock_info", output_dir="output/mn")
    print("✅ Save xlsx for mn completed.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
