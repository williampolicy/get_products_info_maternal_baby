import requests
from bs4 import BeautifulSoup
import time


def get_product_data(keyword):
    url = f'https://www.buybuybaby.com/store/search/search.jsp?query={keyword}'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    print("请求URL：", url)
    print("状态码：", response.status_code)
    
    product_data = []
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', {'class': 'product-grid__item'})

    for item in items:
        product = {}
        product['title'] = item.find('a', {'class': 'product-card__title'}).text.strip()
        product['price'] = item.find('div', {'class': 'product-card__price'}).text.strip()
        product['rating'] = item.find('div', {'class': 'product-card__rating'}).text.strip()
        product['brand'] = item.find('div', {'class': 'product-card__brand'}).text.strip()
        product['url'] = item.find('a', {'class': 'product-card__link'}).get('href')

        print("商品名称：", product['title'])
        print("商品价格：", product['price'])
        print("商品评分：", product['rating'])
        print("商品品牌：", product['brand'])
        print("商品链接：", product['url'])
        print("-" * 50)

        product_data.append(product)
        time.sleep(3)  # 延时 2 秒

    return product_data


if __name__ == '__main__':
    keyword = 'stroller'
    product_data = get_product_data(keyword)
    print(product_data)
