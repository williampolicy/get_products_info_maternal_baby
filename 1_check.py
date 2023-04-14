import requests
from bs4 import BeautifulSoup

url = 'https://list.jd.com/list.html?cat=1318,1462,1482'

response = requests.get(url)

if response.status_code == 200:
    print('成功获取网页内容')
else:
    print('获取网页内容失败')

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
