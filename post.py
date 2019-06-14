# -*- coding: utf-8 -*-
import requests
# 基于requests的post请求
if __name__ == '__main__':

    url = 'https://fanyi.baidu.com/basetrans'
    # post 的请求体
    query_string = {'query':'人生苦短，我用pyhton',
    'from':'zh',
    'to':'en'}
    headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4'}
    # 没加headers请求的时候数据是不对的
    response = requests.post(url,data = query_string,headers = headers)
    # <Response [200]>(虽然是200，但是服务器可能判断我们是一个爬虫依然不给我们响应)
    print response
    print response.content















