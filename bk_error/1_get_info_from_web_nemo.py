from selenium import webdriver
from bs4 import BeautifulSoup

# 设置Chrome webdriver和网站链接
#chrome_driver_path = "/Users/kang/1.live_wit_GPT4/code_pythonanywhere/get_products_info_maternal_baby/chromedriver_mac_arm64"
chrome_driver_path = "/path/to/chromedriver"
url = 'https://www.buybuybaby.com/store/s/toy?ta=typeahead'

# 设置Chrome webdriver选项
options = webdriver.ChromeOptions()
options.add_argument("ignore-certificate-errors")

# 启动Chrome webdriver
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# 获取网页源代码并解析
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 找到所有的产品名并检查是否包含"Nemo"
product_titles = soup.find_all('div', {'class': 'prodTitle'})

for title in product_titles:
    title_text = title.text.strip()
    if "Nemo" in title_text:
        print(f"找到了含有Nemo字段的产品：{title_text}")

# 关闭Chrome webdriver
driver.quit()
