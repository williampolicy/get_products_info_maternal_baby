import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

chrome_driver_path = '/Users/kang/1.live_wit_GPT4/code_pythonanywhere/get_products_info_maternal_baby/chromedriver_mac_arm64/chromedriver"'  # 请将这里替换为您的chromedriver路径
chrome_service = Service(executable_path=chrome_driver_path)

url = 'https://www.buybuybaby.com/store/s/toy?ta=typeahead'

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(url)

try:
    products_locator = (By.CSS_SELECTOR, 'div.prodTitle')
    
    # 模拟滚动页面
    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located(products_locator))

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    product_titles = soup.find_all('div', {'class': 'prodTitle'})
    print(product_titles)
    for title in product_titles:
        title_text = title.text.strip()
        if "Nemo" in title_text:
            print(f"找到了含有Nemo字段的产品：{title_text}")

except Exception as e:
    print("加载页面超时，请检查网络连接或增加等待时间。", e)

finally:
    driver.quit()
