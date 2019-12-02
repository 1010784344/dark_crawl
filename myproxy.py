# -*- coding: UTF-8 -*-
# 使用代理 proxy 请求网站资源

import requests


if __name__ == '__main__':
    url = 'http://httpbin.org/ip'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'}

    proxy = {
        'http':'115.211.43.39:9000'
    }

    response = requests.get(url,headers=headers,proxies = proxy)

    print response.content