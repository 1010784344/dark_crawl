# -*- coding: utf-8 -*-
import requests
# 基于requests的get请求
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'}

    # 请求百度首页没加headers请求的时候数据是不对的
    response = requests.get(url,headers=headers)

    # 输出状态码 200
    print response

    # 输出 html 源码
    print response.content














