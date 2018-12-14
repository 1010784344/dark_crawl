# -*- coding: utf-8 -*-
import requests
# 基于requests的post请求
if __name__ == '__main__':

    url = 'https://fanyi.baidu.com/basetrans'
    # post 的请求体
    query_string = {'query':'人生苦短，我用pyhton',
    'from':'zh',
    'to':'en'}
    response = requests.post(url,data = query_string)
    print response #<Response [200]>(虽然是200，但是服务器可能判断我们是一个爬虫依然不给我们响应)
    print response.content















