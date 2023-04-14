import requests
from lxml import etree
import time

def get_product_data(keyword):
    url = f'https://s.taobao.com/search?q={keyword}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20220819&ie=utf8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    print(f"请求URL：{response.url}")
    print(f"状态码：{response.status_code}")
    print(f"响应内容：{response.text}")
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
    print(product_data)
    time.sleep(2)  # 暂停 2 秒钟
