from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType

chrome_driver_path = "/path/to/chromedriver"

proxy_ip_port = '8.219.176.202:8080'
proxy_settings = {
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_ip_port,
    'sslProxy': proxy_ip_port,
}

options = webdriver.ChromeOptions()
options.add_argument(f"--proxy-server=http://{proxy_ip_port}")
options.add_argument("ignore-certificate-errors")

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


def get_product_data(keyword):
    url = f'https://www.buybuybaby.com/store/s/{keyword}?ta=typeahead'
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    items = soup.find_all('div', {'class': 'product-grid__item'})

    print("找到的商品数量：", len(items))

    product_data = []

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

    return product_data


if __name__ == '__main__':
    keyword = 'toy'
    product_data = get_product_data(keyword)
    print(product_data)
    driver.quit()
