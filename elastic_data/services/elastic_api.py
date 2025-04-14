import os

import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from elastic_data.utils.file_utils import generate_dated_excel_filename


base_url = "https://10.245.65.35:9200/_cat/indices?format=json&pretty&v"

all_indice_data = []

OUTPUT_DIR = "output"

def get_indices():
    headers = {"User-Agent": "Mozilla/5.0"}

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = requests.get(base_url, auth=HTTPBasicAuth('elastic', 'P@ssword'), headers=headers, verify=False)

    if response.status_code == 200:
        data = response.json()
        print(type(data), len(data))

        if isinstance(data, list):
            for item in data:
                all_indice_data.append({
                    "Health": item["health"],
                    "Status": item["status"],
                    "Index": item["index"],
                    "UUID": item["uuid"]
                })
        else:
            print(f"HTTP Error {response.status_code}")

    df = pd.DataFrame(all_indice_data)

    if df.empty:
        print("No Data. Please check API response")
    else:
        print(df.head())
        excel_filename = generate_dated_excel_filename(prefix="indice", output_dir=OUTPUT_DIR)
        df.to_excel(excel_filename, index=False, sheet_name="Indice")

def get_indices_web():
    headers = {"User-Agent": "Mozilla/5.0"}

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = requests.get(base_url, auth=HTTPBasicAuth('elastic', 'P@ssword'), headers=headers, verify=False)

    if response.status_code == 200:
        data = response.json()
        print(type(data), len(data))

        if isinstance(data, list):
            for item in data:
                all_indice_data.append({
                    "Health": item["health"],
                    "Status": item["status"],
                    "Index": item["index"],
                    "UUID": item["uuid"]
                })
        else:
            print(f"HTTP Error {response.status_code}")

    else:
        return f"HTTP Error {response.status_code}: {response.text}"

    df = pd.DataFrame(all_indice_data)

    if df.empty:
        return "No Data. Pleache check API response."

    #HTTP 테이블로 전환
    html_table = df.to_html(classes='table table-striped', index=False, border=0)

    # 간단한 HTML 템플릿
    template = """
    <html>
    <head>
        <title>Indice List</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="container mt-4">
        <h2>Elasticsearch Indices</h2>
        {{ table|safe }}
    </body>
    </html>
    """

    return template, html_table