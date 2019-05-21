# -*- coding: utf-8 -*-
# leg 下载
import requests
from lxml import etree
import urllib
import json
from time import sleep, ctime
import threading




def super_player(pid,pid_url):

    filename = r'D:\outwork\crawl\jpg3\%s.jpg' % pid
    result = urllib.urlretrieve(pid_url, filename)



if __name__ == '__main__':

    base_url = 'http://board.bigbigwork.com/img/listBoardImg?user_token=&uid=90202719&board_id=22621860&page=5&rows=22&like='

    response = requests.get(base_url)
    html_str = response.content.decode('utf-8')
    html_dict = json.loads(html_str)
    strlist = html_dict['list']
    outlist = []
    for strjson in strlist:
        outlist.append(strjson[u'bUrl'])


    print 'Start playing： %s' % ctime()
    # 使用线程
    threads = []
    files = range(len(outlist))
    # 构造线程池
    for pid, pid_url in enumerate(outlist):
        t = threading.Thread(target=super_player, args=(pid,pid_url))
        threads.append(t)

    # 启动线程
    for i in files:
        threads[i].start()

    # join() 方法是表示等这个线程运行完毕，程序再往下运行。
    for i in files:
        threads[i].join()


    print 'end:%s' % ctime()