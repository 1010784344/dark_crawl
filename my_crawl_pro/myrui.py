# -*- coding: utf-8 -*-
# 网页：帮李国瑞同学爬取的设计图片网站
# 类型：单列表页展示
# 方式：简单的get请求

import requests
from lxml import etree
import urllib
from time import sleep
if __name__ == '__main__':

    base_url = 'https://dribbble.com/jeroenvaneerden?page='
    pid = 0
    for i in range(1,47):
        url = base_url + str(i)
        response = requests.get(url)
        html_str = response.content.decode( 'utf-8')
        htmlobj = etree.HTML(html_str)
        pic_list = htmlobj.xpath('//li//source/@srcset')
        print url
        for num,pic in enumerate(pic_list):
            if num%2 == 0:
                pid += 1
                filename = r'D:\outwork\crawl\Dan\%s.jpg' % pid
                result = urllib.urlretrieve(pic, filename)
                sleep(1)


