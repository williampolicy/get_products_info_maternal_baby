

import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType

chrome_driver_path = "/path/to/chromedriver"
#chrome_driver_path = "/Users/kang/1.live_wit_GPT4/code_pythonanywhere/get_products_info_maternal_baby/chromedriver_mac_arm64/chromedriver"


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

# 在这里添加您要查询的关键字
search_keyword = "baby stroller"

# 调用函数，开始搜索
get_product_data_amazon(search_keyword)


# 用于保存数据的列表
data = []

while len(data) < 50:
    time.sleep(2)  # 稍作等待，确保页面已加载

    for item in items:
        if len(data) >= 50:
            break

        try:
            title = item.find("span", class_="a-size-medium a-color-base a-text-normal").text
            price = item.find("span", class_="a-price").find("span", class_="a-offscreen").text
            rating = item.find("span", class_="a-icon-alt").text
            link = item.find("a", class_="a-link-normal a-text-normal")["href"]
            link = f"https://www.amazon.com{link}"
            data.append({"title": title, "price": price, "rating": rating, "link": link})
        except Exception as e:
            pass

    # 导航到下一页
    try:
        next_page = driver.find_element_by_css_selector('.a-pagination .a-last a')
        next_page.click()
        soup = BeautifulSoup(driver.page_source, "html.parser")
        items = soup.find_all("div", {"data-index": True, "data-uuid": True})
    except Exception as e:
        break

# 将数据保存到CSV文件中
with open("baby_strollers.csv", mode="w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["title", "price", "rating", "link"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

# 关闭浏览器
driver.quit()





# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys

# # 设置Chrome浏览器无头模式
# chrome_options = Options()
# chrome_options.add_argument("--headless")

# # 在这里输入您的Chrome WebDriver路径
# chrome_driver_path = "path/to/chromedriver"

# # 启动浏览器
# driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# # 访问Amazon
# url = "https://www.amazon.com"
# driver.get(url)

# # 搜索baby stroller
# search_box = driver.find_element_by_id("twotabsearchtextbox")
# search_box.send_keys("baby stroller")
# search_box.send_keys(Keys.RETURN)

# # 用于保存数据的列表
# data = []

# while len(data) < 50:
#     time.sleep(2)  # 稍作等待，确保页面已加载
#     products = driver.find_elements_by_css_selector(".s-result-item")

#     for product in products:
#         if len(data) >= 50:
#             break

#         try:
#             title = product.find_element_by_css_selector(".a-link-normal .a-text-normal").text
#             price = product.find_element_by_css_selector(".a-price .a-offscreen").text
#             rating = product.find_element_by_css_selector(".a-icon-alt").text
#             link = product.find_element_by_css_selector(".a-link-normal .a-text-normal").get_attribute("href")
#             data.append({"title": title, "price": price, "rating": rating, "link": link})
#         except Exception as e:
#             pass

#     # 导航到下一页
#     try:
#         next_page = driver.find_element_by_css_selector('.a-pagination .a-last a')
#         next_page.click()
#     except Exception as e:
#         break

# # 将数据保存到CSV文件中
# with open("baby_strollers.csv", mode="w", newline='', encoding="utf-8") as csvfile:
#     fieldnames = ["title", "price", "rating", "link"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)

# # 关闭浏览器
# driver.quit()

