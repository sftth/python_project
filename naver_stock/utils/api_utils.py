import platform
from datetime import datetime



def append_data(data, firm, category, name, stock_code):
    # 운영체제에 따라 날짜 포맷 선택
    if platform.system() == "Windows":
        date_format = "%Y.%#m.%#d"
    else:  # macOS, Linux
        date_format = "%Y.%-m.%-d"

    all_stock_data = []
    if isinstance(data, list):
        for item in data:
            all_stock_data.append({
                "NO": "",
                "Firm": firm,
                "Type": category,
                "Name": name,
                "Code": stock_code,
                "Date": datetime.strptime(item["localTradedAt"][:10], "%Y-%m-%d"),
                "Price": float(item["closePrice"].replace(",", "")),  # 쉼표 제거 후 정수 변환
                "Change": float(item["compareToPreviousClosePrice"].replace(",", "")),  # ✅ 쉼표 제거 후 int 변환
                "Rate (%)": float(item["fluctuationsRatio"]) * 0.01,  # 등락률은 소수점 필요
                "Open": float(item["openPrice"].replace(",", "")),
                "High": float(item["highPrice"].replace(",", "")),
                "Low": float(item["lowPrice"].replace(",", ""))
            })
    return all_stock_data