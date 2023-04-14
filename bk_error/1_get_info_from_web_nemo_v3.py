import requests
from bs4 import BeautifulSoup

url = 'https://www.buybuybaby.com/store/s/toy?ta=typeahead'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_titles = soup.find_all('div', {'class': 'prodTitle'})
    print(product_titles)
    for title in product_titles:
        title_text = title.text.strip()
        if "Nemo" in title_text:
            print(f"找到了含有Nemo字段的产品：{title_text}")
else:
    print("无法获取网页，请检查网络连接或尝试稍后再试。")
