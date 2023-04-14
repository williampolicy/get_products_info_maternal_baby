import requests
from fake_useragent import UserAgent
from lxml import etree
import time

def get_product_data(keyword):
    ua = UserAgent()
    url = f'https://s.taobao.com/search?q={keyword}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20220819&ie=utf8'
    headers = {
        'User-Agent': ua.random,
        'Referer': 'https://www.taobao.com/',
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)

    product_data = []
    for item in html.xpath('//div[@class="item J_MouserOnverReq  "]'):
        product = {}
        product['title'] = item.xpath('.//a[@class="title"]/@title')[0]
        product['price'] = item.xpath('.//strong/text()')[0]
        product['location'] = item.xpath('.//div[@class="location"]/text()')[0]
        product_data.append(product)

    return product_data

if __name__ == '__main__':
    keyword = 'iphone'
    product_data = get_product_data(keyword)
    while not product_data:
        print('未获取到商品数据')
        time.sleep(2)
        product_data = get_product_data(keyword)
    print(product_data)
