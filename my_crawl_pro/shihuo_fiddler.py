# -*- coding: utf-8 -*-
import os
import json
from time import sleep
import requests
import urllib
# 利用 fiddler 抓包工具，查看接口，访问应用宝里面的数据交互
path = 'D:/shihou/AJ1/'
if not os.path.exists(path):
    os.mkdir(path)
requests.packages.urllib3.disable_warnings()
if __name__ == '__main__':
    url = 'https://www.shihuo.cn/app_swoole_shoe/getStyles?channel=default&clientCode=865166024517362&id=13&page=9&page_size=20&platform=android&size=&style_id=804062%2C913140%2C974068%2C584241%2C915733%2C877508%2C592717%2C599306&timestamp=1573462800000&token=e4ecf4d0710215af8263fa61e4834641&v=6.4.4'
    headers = {'User-Agent':'Android5.1.1 xiaomi CPU_ABI armeabi-v7a CPU_ABI2 armeabi HARDWARE android_x86 MODEL xiaomi 8 shihuo/5.4.1','Accept-Encoding':'gzip','Host':'www.shihuo.cn','Connection':'Keep-Alive','Cookie':'_shcid=LUDWVrjsck6RABZXC1YS'}

    response = requests.get(url,verify=False)

    html_str = response.content

    htm = json.loads(html_str)


    imgurls = htm['data']['list']
    print len(imgurls)
    for img in imgurls:
        id = img['id']
        imgurl = img['img']
        # imglist.append(imgurl)
        print imgurl
        filename = path + id + '.jpg'
        result = urllib.urlretrieve(imgurl, filename)
        sleep(2)













