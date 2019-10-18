# -*- coding: utf-8 -*-
# 网页：什么值得买
# 类型：主列表和子列表
# 方式：简单的get请求

import os
import requests
import urllib
from time import sleep
from lxml import etree
import logging
logging.basicConfig(level=logging.INFO, format=None)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'}


def detailimg(url,outdir):

    response = requests.get(url, headers=headers)

    html_str = response.content.decode('utf-8')

    htmlobj = etree.HTML(html_str)
    html_list = htmlobj.xpath('//p[@itemprop="description"]//img/@src')
    for item in html_list:
        name = item.split('/')[-1]
        logging.info(name)
        filename = outdir + '\%s' % name
        result = urllib.urlretrieve(item, filename)
        sleep(2)


if __name__ == '__main__':

    base_listurl = 'https://post.smzdm.com/fenlei/yundongxiewa'
    base_dir = r'D:\outwork\crawl\jpg3'
    for i in range(1,11):
        pnum = '/p%s/'%i
        listurl = base_listurl + pnum

        response = requests.get(listurl,headers=headers)

        html_str = response.content.decode('utf-8')

        htmlobj = etree.HTML(html_str)
        html_list = htmlobj.xpath('//h2[@class="item-name"]/a/@href')

        outdir = base_dir + '\%s'%i
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        for item in html_list:
            try:
                detailimg(item,outdir)
            except Exception as e:
                logging.info(e)






















