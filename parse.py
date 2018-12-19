# -*- coding: utf-8 -*-
# 容错机制：超时和重试

from retrying import retry
import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'}
headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4',
           'Referer':'https://m.douban.com/tv/'}
# 让装饰函数反复执行3次，3次全部报错才会报错，中间有一次正常，程序继续往后走
@retry(stop_max_attempt_number=3)
def _parse_url(url):
    print '*'*50
    response = requests.get(url,headers=headers,timeout=3)
    return response.content.decode('utf-8')

def parse_url(url):
    try:
        html = _parse_url(url)
    except:
        html = None
    return html

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    url1 = 'www.baidu.cm'
    print parse_url(url)[:100]







