from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 设置Chrome webdriver和网站链接
chrome_driver_path = "/path/to/chromedriver"
url = 'https://www.buybuybaby.com/store/s/toy?ta=typeahead'

# 设置Chrome webdriver选项
options = webdriver.ChromeOptions()
options.add_argument("ignore-certificate-errors")

# 启动Chrome webdriver
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# 获取网页源代码并解析
driver.get(url)

# 等待加载所有产品
products_locator = (By.CLASS_NAME, 'product-grid__item')
WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located(products_locator))

# 解析加载完毕的网页
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 找到所有的产品名并检查是否包含"Nemo"
product_titles = soup.find_all('div', {'class': 'prodTitle'})

for title in product_titles:
    title_text = title.text.strip()
    if "Nemo" in title_text:
        print(f"找到了含有Nemo字段的产品：{title_text}")

# 关闭Chrome webdriver
driver.quit()
