from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType

chrome_driver_path = "/path/to/chromedriver"

# 更换为您要使用的代理 IP 和端口
proxy_ip_port = '8.219.176.202:8080'

proxy_settings = {
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_ip_port,
    'sslProxy': proxy_ip_port,
}

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % proxy_ip_port)
options.add_argument("ignore-certificate-errors")

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

def get_product_data_amazon(keyword):
    base_url = "https://www.amazon.com"
    search_url = f"{base_url}/s?k={keyword.replace(' ', '+')}"
    
    driver.get(search_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all("div", {"data-index": True, "data-uuid": True})

    print("找到的商品数量：", len(items))

    product_data = []

    for item in items:
        product = {}
        try:
            product['title'] = item.find("span", {"class": "a-size-medium"}).text.strip()
            product['url'] = base_url + item.find("a", {"class": "a-link-normal"})["href"]
            product['price'] = item.find("span", {"class": "a-price"}).text.strip()
            product['rating'] = item.find("span", {"class": "a-icon-alt"}).text.strip()
            product_data.append(product)
            print("商品名称：", product['title'])
            print("商品价格：", product['price'])
            print("商品评分：", product['rating'])
            print("商品链接：", product['url'])
            print("-" * 50)
        except AttributeError:
            continue

    driver.quit()
    return product_data

if __name__ == "__main__":
    keyword = "baby stroller"
    product_data = get_product_data_amazon(keyword)
    print(product_data)
