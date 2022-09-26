from lxml import etree
import requests
import execjs
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

def spider(url):
    comnent = []
    r = requests.get(url=url, headers=headers)
    selector = etree.HTML(r.text)
    for i in range(1, 100):
        comnent.extend(selector.xpath(f'//*[@id="content"]/p[{i}]/span/text()'))
    print(comnent)
    return comnent

