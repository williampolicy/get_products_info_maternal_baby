from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy_ip_port = '8.219.176.202:8080'

proxy_settings = {
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_ip_port,
    'sslProxy': proxy_ip_port,
}

proxy = Proxy(proxy_settings)
chrome_options = webdriver.ChromeOptions()
chrome_options.Proxy = proxy
chrome_options.add_argument('--proxy-server=%s' % proxy_ip_port)

chrome_driver_path = '/Users/kang/1.live_wit_GPT4/code_pythonanywhere/get_products_info_maternal_baby/to/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get('https://www.buybuybaby.com/')
