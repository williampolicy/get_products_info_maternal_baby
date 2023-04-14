import requests

url = "https://api.buybuybaby.com/v1/products"
params = {
    "category": "3100001",  # 母婴产品分类
    "count": "50",  # 获取50个商品信息
    "sort": "popularity-desc",  # 按热度降序排序
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Referer": "https://www.buybuybaby.com/",
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    products = response.json()["products"]
    for product in products:
        print(product["productName"])
else:
    print("请求失败，错误代码：", response.status_code)
