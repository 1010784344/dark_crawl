# -*- coding: utf-8 -*-
import requests
# 基于requests的get请求
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'}
    response = requests.get(url,headers=headers)
    # 请求百度首页没加headers请求的时候数据是不对的
    response = requests.get(url)
    print response #<Response [200]>
    # 输出有乱码，因为当我们使用response.text的时候，他的解码格式是request根据他的响应头部猜
    # 出来的。到时候request模块就会按照这个编码方式，去对他进行解码
    # response.encoding = 'utf-8'
    # print response.text

    print response.content














