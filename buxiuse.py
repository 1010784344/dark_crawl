# -*- coding: utf-8 -*-
# leg 下载
import requests
from lxml import etree
import urllib

if __name__ == '__main__':
    num = 1
    # base_url = 'https://www.dbmeinv.com/index.htm?cid=6&pager_offset='
    base_url = 'https://www.dbmeinv.com/index.htm?cid=3&pager_offset='
    pid = 0
    while num:

        url = base_url + str(num)
        response = requests.get(url)
        html_str = response.content.decode('utf-8')
        # print html_str

        htmlobj = etree.HTML(html_str)
        pic_list = htmlobj.xpath('//div[@class="img_single"]//@src')

        # print pic_list

        for pic in pic_list:
            pid += 1
            filename = r'D:\outwork\crawl\jpg3\%s.jpg'%pid
            result = urllib.urlretrieve(pic,filename)

        pic_judge = htmlobj.xpath('//li[@class="next next_page"]/a')
        if not pic_judge:
            break
        num += 1