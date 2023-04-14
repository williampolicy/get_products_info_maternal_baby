import requests
from bs4 import BeautifulSoup
import random
import time


def get_product_data(keyword):
    headers_list = [
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Referer': 'https://www.buybuybaby.com/store/s/'+keyword+'?q='+keyword
        },
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Referer': 'https://www.buybuybaby.com/store/s/'+keyword
        },
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Referer': 'https://www.buybuybaby.com/store/s/'+keyword+'?sort=&page=&keywords='+keyword
        }
    ]

    headers = random.choice(headers_list)
    url = 'https://www.buybuybaby.com/store/s/'+keyword+'?sort=&page=&keywords='+keyword
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    product_data = []
    for item in soup.select('.product-grid-tile .product-card-wrapper'):
        product = {}
        product['title'] = item.select_one('.product-card-title a').get_text().strip()
        product['price'] = item.select_one('.product-card-price').get_text().strip()
        product['location'] = item.select_one('.product-card-brand').get_text().strip()
        product_data.append(product)

    return product_data


if __name__ == '__main__':
    keyword = 'stroller'
    product_data = get_product_data(keyword)
    print(product_data)
