import requests
import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side, NamedStyle
from naver_stock.utils.file_utils import generate_dated_excel_filename

# ✅ 조회할 종목 리스트
stock_list = [
["stock","LG에너지솔루션","373220"],
["stock","LG전자","066570"],
["stock","NAVER","035420"],
["stock","SK리츠","395400"],
["stock","TIGER배당커버드콜액티브","472150"],
["stock","TIGER은행고배당플러스 TOP10","466940"],
["stock","그래디언트","035080"],
["stock","대원미디어","048910"],
["stock","에스디바이오센서","137310"],
["stock","웅진씽크빅","095720"],
["stock","카카오","035720"],
["stock","카카오게임즈","293490"],
["stock","카카오뱅크","323410"],
["stock","펄어비스","263750"]
]

stock_list_us = [
["etf","YieldMax COIN Option Income Strategy ETF","CONY.K"],
["etf","2x Bitcoin Strategy ETF","BITX.K"]
]

OUTPUT_DIR = "output"

# ✅ API 기본 URL
base_url = "https://m.stock.naver.com/api/{}/{}/price?pageSize=1&page=1"
base_url_us = "https://api.stock.naver.com/{}/{}/price?page=1&pageSize=1"

# ✅ 데이터 저장할 리스트 생성
all_stock_data = []

# ✅ 각 종목별 데이터 요청
headers = {"User-Agent": "Mozilla/5.0"}

def fetch_stock_data(stock_list, base_url):
    stock_data = []

    for category, name, stock_code in stock_list:
        url = base_url.format(category, stock_code)

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    for item in data:
                        stock_data.append({
                            "공백": "",
                            "증권사": "HT",
                            "카테고리":category,
                            "이름":name,
                            "종목 코드": stock_code,
                            "거래 날짜": item["localTradedAt"][:10],  # YYYY-MM-DD 형식으로 자르기
                            "종가": float(item["closePrice"].replace(",", "")),  # 쉼표 제거 후 정수 변환
                            "전일 대비": float(item["compareToPreviousClosePrice"].replace(",", "")),  # ✅ 쉼표 제거 후 int 변환
                            "등락률 (%)": float(item["fluctuationsRatio"]) * 0.01,  # 등락률은 소수점 필요
                            "시가": float(item["openPrice"].replace(",", "")),  
                            "고가": float(item["highPrice"].replace(",", "")),  
                            "저가": float(item["lowPrice"].replace(",", ""))
                        })
            else:
                print(f"⛔ {stock_code} 데이터 가져오기 실패 (HTTP {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"⛔ {stock_code} 데이터 가져오기 실패: {e}")
    return stock_data

def ht_save_xlsx():
    # KR & US stock data
    all_stock_data = fetch_stock_data(stock_list, base_url) + fetch_stock_data(stock_list_us, base_url_us)


    # ✅ 데이터프레임 변환
    df = pd.DataFrame(all_stock_data)

    if df.empty:
        print("⚠️ 데이터가 없습니다. API 응답을 확인하세요.")
#    else:
#        print(df.head())  # ✅ 데이터가 들어있는지 확인

    # ✅ 엑셀 파일로 저장
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    excel_filename = generate_dated_excel_filename(prefix="ht", output_dir=OUTPUT_DIR)
#    excel_filename = "ht_stocks_data_v1.1.xlsx"
    df.to_excel(excel_filename, index=False, sheet_name="Stock Prices")

    # ✅ 엑셀 파일 불러와 서식 적용
    wb = load_workbook(excel_filename)
    ws = wb["Stock Prices"]

    # ✅ 스타일 설정
    header_font = Font(name="Calibri", bold=True, size=12, color="FFFFFF")  # 제목 폰트
    header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")  # 제목 배경색
    thin_border = Border(left=Side(style="thin"), right=Side(style="thin"), top=Side(style="thin"), bottom=Side(style="thin"))
    center_align = Alignment(horizontal="center", vertical="center")

    # ✅ 숫자 스타일 지정
    currency_style = NamedStyle(name="currency_style", number_format="#,##0")
    percent_style = NamedStyle(name="percent_style", number_format="0.00%")
    date_style = NamedStyle(name="date_style", number_format="YYYY-MM-DD")

    # ✅ 스타일을 워크북에 추가 (기존 스타일 중복 방지)
    if "currency_style" not in wb.named_styles:
        wb.add_named_style(currency_style)
    if "percent_style" not in wb.named_styles:
        wb.add_named_style(percent_style)
    if "date_style" not in wb.named_styles:
        wb.add_named_style(date_style)

    # ✅ 헤더 스타일 적용
    for cell in ws[1]:
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    # ✅ 데이터 셀 스타일 적용
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
        row[5].style = date_style  # 날짜 형식 적용
        row[6].style = currency_style  # 종가 형식 적용
        row[7].style = currency_style  # 전일 대비 형식 적용
        row[8].style = percent_style  # 등락률(%) 형식 적용
        row[9].style = currency_style  # 시가 형식 적용
        row[10].style = currency_style  # 고가 형식 적용
        row[11].style = currency_style  # 저가 형식 적용

    # ✅ 엑셀 파일 저장
    wb.save(excel_filename)
    wb.close() # 파일 닫기
    print(f"✅ 모든 종목 데이터가 엑셀에 저장 완료 (서식 적용): {excel_filename}")
