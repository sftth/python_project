import requests
import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side, NamedStyle
from datetime import datetime
from naver_stock.utils.file_utils import generate_dated_excel_filename

# ✅ 조회할 종목 리스트
stock_list = [
["대한항공","003490"],
["두산에너빌리티","034020"],
["디어유","376300"],
["삼성전자","005930"],
["삼성중공업","010140"],
["쏠리드","050890"],
["에코프로비엠","247540"],
["코오롱티슈진","950160"],
["포스코인터내셔널","047050"],
["포스코퓨처엠","003670"],
["한국항공우주","047810"],
["한화솔루션","009835"],
["한화에어로스페이스","012450"],
["한화오션","042660"],
["현대로템","064350"],
["현대차","005380"],
["현대ADM","187660"],
["후성","093370"],
["HPSP","403870"],
["KODEX 미디어&엔터테인먼트","266360"],
["KODEX 코스닥150레버리지","233740"],
["LG생활건강","051900"],
["LG씨엔에스","064400"],
["LG전자","066570"],
["LS에코에너지","229640"],
["Plus 한화그룹주","0000J0"],
["POSCO홀딩스","005490"],
["SAMG엔터","419530"],
["SK하이닉스","000660"],
["SOL 조선 TOP3플러스","466920"],
["TIGER 200에너지화학레버리지","243890"],
["TIGER 미국나스닥100커버드콜(합성)","441680"],
["TIGER 미국S&P500","360750"]
]

OUTPUT_DIR = "output"

# ✅ API 기본 URL
base_url = "https://m.stock.naver.com/api/stock/{}/price?pageSize=1&page=1"

# ✅ 데이터 저장할 리스트 생성
all_stock_data = []

def nh_save_xlsx():
    # ✅ 각 종목별 데이터 요청
    headers = {"User-Agent": "Mozilla/5.0"}
    for name, stock_code in stock_list:
        url = base_url.format(stock_code)
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                for item in data:
                    all_stock_data.append({
                        "공백": "",
                        "증권사": "NH",
                        "Type":"",
                        "이름":name,
                        "종목 코드": stock_code,
                        "거래 날짜": datetime.strptime(item["localTradedAt"][:10], "%Y-%m-%d").strftime("%Y.%m.%d"),
                        "종가": int(item["closePrice"].replace(",", "")),  # 쉼표 제거 후 정수 변환
                        "전일 대비": int(item["compareToPreviousClosePrice"].replace(",", "")),  # ✅ 쉼표 제거 후 int 변환
                        "등락률 (%)": float(item["fluctuationsRatio"]) * 0.01,  # 등락률은 소수점 필요
                        "시가": int(item["openPrice"].replace(",", "")),
                        "고가": int(item["highPrice"].replace(",", "")),
                        "저가": int(item["lowPrice"].replace(",", ""))
                    })
        else:
            print(f"⛔ {stock_code} 데이터 가져오기 실패 (HTTP {response.status_code})")

    # ✅ 데이터프레임 변환
    df = pd.DataFrame(all_stock_data)

    # ✅ 엑셀 파일로 저장
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    excel_filename = generate_dated_excel_filename(prefix="nh", output_dir=OUTPUT_DIR)
#    excel_filename = "nh_stocks_data_v1.1.xlsx"
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
    currency_style = NamedStyle(name="currency_style", number_format=r'_(₩* #,##0_);_(₩* (#,##0);_(₩* "-"_);_(@_)')
    percent_style = NamedStyle(name="percent_style", number_format="0.00%")
    date_style = NamedStyle(name="date_style", number_format="yyyy.mm.dd")

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
        row[1].alignment = center_align
        row[5].alignment = center_align
        row[5].style = date_style  # 날짜 형식 적용
        row[6].style = currency_style  # 종가 형식 적용
        row[7].style = currency_style  # 전일 대비 형식 적용
        row[8].style = percent_style  # 등락률(%) 형식 적용
        row[9].style = currency_style  # 시가 형식 적용
        row[10].style = currency_style  # 고가 형식 적용
        row[11].style = currency_style  # 저가 형식 적용

    # ✅ 엑셀 파일 저장
    wb.save(excel_filename)
    print(f"✅ 모든 종목 데이터가 엑셀에 저장 완료 (서식 적용): {excel_filename}")
