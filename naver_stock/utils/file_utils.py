import os
from datetime import datetime
from openpyxl import Workbook

def generate_dated_excel_filename(prefix="stock", output_dir="output"):
    """
    날짜 기반 파일명을 사용해 엑셀 파일을 저장하는 공통 함수.
    예: ht-2025.04.10.xlsx, nh-2025.04.10.xlsx

    :param data: dict 형태로 엑셀에 넣을 데이터 (key: 셀, value: 값)
    :param prefix: 파일명 접두어 ('ht', 'mn', 'nh' 등)
    :param output_dir: 저장 디렉토리 경로
    :return: 저장된 파일 경로 (str)
    """
    os.makedirs(output_dir, exist_ok=True)

    today_str = datetime.today().strftime("%Y.%m.%d")
    filename = f"{prefix}-{today_str}.xlsx"
    return os.path.join(output_dir, filename)