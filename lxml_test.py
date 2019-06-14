# -*- coding: utf-8 -*-
import requests
from lxml import etree

import sys

reload(sys)

sys.setdefaultencoding("utf-8")

url = 'https://movie.douban.com/chart'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'}

if __name__ == '__main__':
    response = requests.get(url,headers=headers)
    html_str = response.content.decode('utf-8')
    # print html_str

    htmlobj = etree.HTML(html_str)
    # 1.获取所有电影的url地址
    # link_list = htmlobj.xpath('//div[@class="pl2"]/a/@href')
    # print link_list

    # 2.获取所有图片的url地址
    # pic_list = htmlobj.xpath('//a[@class="nbg"]//@src')
    # print pic_list

    # 3.需要把每部电影组成一个字典，字典中是电影重要的数据，比如标题，url，图片地址，评论数，评分
    # 思路：
        # 1.分组
        # 2. 每一组提取数据

    for table in htmlobj.xpath('//table[@width="100%"]'):
        item = {}
        item['title'] = table.xpath('.//a[@class="nbg"]/@title')[0]
        item['url'] = table.xpath('.//div[@class="pl2"]/a/@href')[0]
        item['image'] = table.xpath('.//a[@class="nbg"]//@src')[0]
        item['rating'] = table.xpath('.//span[@class="rating_nums"]/text()')[0]
        item['comment'] = table.xpath('.//span[@class="pl"]/text()')[0]
        print item

#<span class="format-time">1天前发布</span>,这种获取文字不是属性要加“/text()”
# 如果获取的是属性的值就不用加“/text()”








