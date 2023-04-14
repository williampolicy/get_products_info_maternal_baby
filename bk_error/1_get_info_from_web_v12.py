from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.proxy import Proxy, ProxyType

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 设置Chrome webdriver和网站链接
chrome_driver_path = "/path/to/chromedriver"
url = 'https://www.buybuybaby.com/store/s/toy?ta=typeahead'

# 设置代理
# proxy_ip_port = '8.219.176.202:8080'
# proxy_settings = {
#     'proxyType': ProxyType.MANUAL,
#     'httpProxy': proxy_ip_port,
#     'sslProxy': proxy_ip_port,
# }



# 设置Chrome webdriver选项
options = webdriver.ChromeOptions()
#options.add_argument(f"--proxy-server=http://{proxy_ip_port}")
options.add_argument("ignore-certificate-errors")

# 启动Chrome webdriver
#driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver = webdriver.Chrome(options=options)


# 获取网页源代码并解析
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
with open('soup_prettify.md', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# 找到所有宝宝玩具列表项并抓取信息


# 找到所有宝宝玩具列表项并抓取信息
items_locator = (By.CLASS_NAME, 'product-grid__item')
WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located(items_locator))
items = driver.find_elements(*items_locator)

#items = soup.find_all('div', {'class': 'product-grid__item'})
product_data = []
print('-------')

for item in items:
    title = item.find('a', {'class': 'product-card__title'}).text.strip()
    price = item.find('div', {'class': 'product-card__price'}).text.strip()
    print(f"标题：{title}，价格：{price}")

product_data = []
for item in items:
    product = {}
    product['title'] = item.find('a', {'class': 'product-card__title'}).text.strip()
    product['price'] = item.find('div', {'class': 'product-card__price'}).text.strip()
    product['rating'] = item.find('div', {'class': 'product-card__rating'}).text.strip()
    product['brand'] = item.find('div', {'class': 'product-card__brand'}).text.strip()
    product['url'] = item.find('a', {'class': 'product-card__link'}).get('href')
    product_data.append(product)

print(product_data) # 打印产品数据


for item in items:
    product = {}
    product['title'] = item.find('a', {'class': 'product-card__title'}).text.strip()
    if "Nemo" in product['title']:
        print("找到了含有Nemo字段的产品：", product['title'])
    product['price'] = item.find('div', {'class': 'product-card__price'}).text.strip()
    product['rating'] = item.find('div', {'class': 'product-card__rating'}).text.strip()
    product['brand'] = item.find('div', {'class': 'product-card__brand'}).text.strip()
    product['url'] = item.find('a', {'class': 'product-card__link'}).get('href')
    product_data.append(product)


for item in items:
    product = {}
    product['title'] = item.find('a', {'class': 'product-card__title'}).text.strip()
    product['price'] = item.find('div', {'class': 'product-card__price'}).text.strip()
    product['rating'] = item.find('div', {'class': 'product-card__rating'}).text.strip()
    product['brand'] = item.find('div', {'class': 'product-card__brand'}).text.strip()
    product['url'] = item.find('a', {'class': 'product-card__link'}).get('href')
    product_data.append(product)

# 将抓取到的数据转换为pandas DataFrame，并输出为CSV文件
df = pd.DataFrame(product_data)
df.to_csv('buybuybaby_toy.csv', index=False)

# 关闭Chrome webdriver
driver.quit()
