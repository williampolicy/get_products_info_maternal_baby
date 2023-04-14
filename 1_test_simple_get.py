import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager

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

# 使用 ChromeDriverManager() 类来自动下载合适版本的 chromedriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


def get_product_data_amazon(keyword):
    base_url = "https://www.amazon.com"
    search_url = f"{base_url}/s?k={keyword.replace(' ', '+')}"

    driver.get(search_url)
    
    # 用于保存数据的列表
    data = []
    count = 0
    
    while True:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        items = soup.find_all("div", {"data-index": True, "data-asin": True})
        # items = soup.find_all("div", {"data-index": True, "data-uuid": True})
        #items = soup.find_all("div", class_=["a-section", "s-product-header"])
        items = soup.find_all("div", class_=["s-result-item", "s-asin", "s-border-bottom", "s-widget"])

        count += len(items)
        print(f"Found {len(items)} items on this page")
        
        for item in items:
            try:
                title = item.find("span", class_="a-size-medium a-color-base a-text-normal").text
                price = item.find("span", class_="a-price").find("span", class_="a-offscreen").text
                rating = item.find("span", class_="a-icon-alt").text
                link = item.find("a", class_="a-link-normal a-text-normal")["href"]
                link = f"https://www.amazon.com{link}"
                data.append({"title": title, "price": price, "rating": rating, "link": link})
            except Exception as e:
                pass
            print(f"-------Found {len(data)} items in total")

        if count >= 50:
            break

        # 点击下一页
        try:
            next_button = driver.find_element_by_xpath("//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-disabled' and @aria-disabled='true']")
        except:
            next_button = driver.find_element_by_xpath("//a[@class='s-pagination-item s-pagination-next s-pagination-button']")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(5)

    # 将数据保存到CSV文件
    with open(f"{keyword}.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "price", "rating", "link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)

    driver.quit()


get_product_data_amazon("baby stroller")
