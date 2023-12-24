import requests
import pandas as pd

def get_data_from_api(api_url, offset, limit):
    params = {
        'tokenAddress': '0x8C630bD3a6B58fD26F246E5EB74837fFCcE6C5bE',
        'offset': offset,
        'limit': limit
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data.get("data", [])

def write_to_excel(data, excel_file):
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False, engine='openpyxl')

def main():
    api_url = "https://www.vicscan.xyz/api/nft/inventory"
    excel_file = "nft_data.xlsx"
    limit_per_page = 100
    total_items = 10000

    all_data = []

    # Lặp qua từng trang để lấy dữ liệu
    for offset in range(0, total_items, limit_per_page):
        # Lấy dữ liệu từ API
        nft_data = get_data_from_api(api_url, offset, limit_per_page)
        all_data.extend(nft_data)

    # Ghi dữ liệu vào file Excel
    write_to_excel(all_data, excel_file)

if __name__ == "__main__":
    main()
