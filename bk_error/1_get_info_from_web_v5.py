from selenium import webdriver
from bs4 import BeautifulSoup



from selenium import webdriver

chrome_driver_path = "/Users/kang/1.live_wit_GPT4/code_pythonanywhere/get_products_info_maternal_baby/to/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy_ip_port = '8.219.176.202:8080'

proxy_settings = {
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_ip_port,
    'sslProxy': proxy_ip_port,
}


# proxy = Proxy({
#     'proxyType': ProxyType.MANUAL,
#     'httpProxy': 'http://your_proxy_ip:your_proxy_port',
#     'sslProxy': 'http://your_proxy_ip:your_proxy_port',
# })

options = webdriver.ChromeOptions()
options.Proxy = proxy
options.add_argument("ignore-certificate-errors")

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


def get_product_data(keyword):
    url = f'https://www.buybuybaby.com/store/search/search.jsp?query={keyword}'
    
    driver = webdriver.Chrome()  # 使用 Chrome 驱动
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

    driver.quit()

    return product_data


if __name__ == '__main__':
    keyword = 'baby stroller'
    product_data = get_product_data(keyword)
    print(product_data)





# IP Address  Port    Code    Country Anonymity   Google  Https   Last Checked
# 8.210.83.33 80  HK  Hong Kong   anonymous   yes no  1 min ago
# 8.219.176.202   8080    SG  Singapore   elite proxy no  yes 1 min ago
# 137.184.245.154 80  US  United States   anonymous   yes no  1 min ago
# 103.219.193.174 80  US  United States   anonymous   no  no  1 min ago
# 139.99.237.62   80  AU  Australia   anonymous   yes no  1 min ago
# 154.118.228.212 80  TZ  Tanzania    anonymous   no  no  1 min ago
