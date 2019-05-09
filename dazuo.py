# -*- coding: utf-8 -*-
# leg 下载
import requests
from lxml import etree
import urllib
import json
from time import sleep, ctime

if __name__ == '__main__':
    num = 1
    # base_url = 'https://www.dbmeinv.com/index.htm?cid=6&pager_offset='
    base_url = 'http://board.bigbigwork.com/img/listBoardImg?user_token=&uid=90202719&board_id=22621860&page=3&rows=22&like='

    response = requests.get(base_url)
    html_str = response.content.decode('utf-8')
    html_dict = json.loads(html_str)
    strlist = html_dict['list']
    outlist = []
    for strjson in strlist:
        outlist.append(strjson[u'bUrl'])


    pid = 0
    print 'Start playing： %s' % ctime()
    for pic in outlist:
        filename = r'D:\outwork\crawl\jpg3\%s.jpg'%pid
        result = urllib.urlretrieve(pic,filename)
        pid  += 1

    print 'end:%s' % ctime()