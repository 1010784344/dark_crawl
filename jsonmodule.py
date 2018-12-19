# -*- coding: utf-8 -*-
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

url = 'https://m.douban.com/rexxar/api/v2/subject_collection/tv_variety_show/items?os=ios&start=0&count=8&loc_id=108288&_=1545115479163'
headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4',
           'Referer':'https://m.douban.com/tv/'}

if __name__ == '__main__':
    response = requests.get(url,headers=headers)
    json_str = response.content.decode('utf-8')
    str1 = json.loads(json_str)
    # 将字典转换为字符串的时候，不要将中文以 ascii 的形式编码
    # indent 参数能够让我们保持写入文本的时候下一行在上一行的基础上空4格，起到美化的效果
    str = json.dumps(str1, ensure_ascii=False,indent=2)
    with open('json.txt','w') as f:
        f.write(str)
