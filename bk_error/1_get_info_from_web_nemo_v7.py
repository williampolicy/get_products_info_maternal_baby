import requests
import json

url = 'https://www.buybuybaby.com/store/product/search?searchTerm=toy&ta=typeahead&start=0&count=100'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    products = data['products']

    for product in products:
        product_name = product['displayName']
        if "Nemo" in product_name:
            print(f"找到了含有Nemo字段的产品：{product_name}")
else:
    print("无法获取网页，请检查网络连接或尝试稍后再试。")
