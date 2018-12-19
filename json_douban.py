# -*- coding: utf-8 -*-
from parse import parse_url
import json

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Douban(object):
    def __init__(self):
        self.baseurl = 'https://m.douban.com/rexxar/api/v2/subject_collection/tv_variety_show/items?os=ios&count=8&loc_id=108288&_=1545115479163&start='
    def getdata(self,html_str):
        htm = json.loads(html_str)
        htm_data = htm['subject_collection_items']
        total = htm['total']
        print total
        return htm_data,total
    def savedata(self,strdata):
        with open('douban.txt','a') as f:
            for data in strdata:
                f.write(json.dumps(data,ensure_ascii=False))
                f.write('\n')

    def run(self):
        #1.请求startsurl页面
        num = 0
        total = 1
        while num < total:
            # 1.start_url
            url = self.baseurl + str(num)
            # 2.发送请求，获取响应
            htm_str = parse_url(url)
            #3.提取数据
            strdata,total = self.getdata(htm_str)
            #4.保存
            self.savedata(strdata)
            #5.构造下一页的url地址，循环第2-5步
            num = num + 8
if __name__ == '__main__':
    douban = Douban()
    douban.run()