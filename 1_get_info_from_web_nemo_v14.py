import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.buybuybaby.com/store/s/toy?ta=typeahead'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_titles = soup.find_all('div', {'class': 'prodTitle'})
    print('----------')
    print(product_titles)

    time.sleep(5)  # 延迟5秒以便页面数据加载

    # 再次查找产品标题
    product_titles = soup.find_all('div', {'class': 'prodTitle'})
    print('----------')
    print(product_titles)

    for title in product_titles:
        title_text = title.text.strip()
        if "Nemo" in title_text:
            print(f"找到了含有Nemo字段的产品：{title_text}")
else:
    print("无法获取网页，请检查网络连接或尝试稍后再试。")
