# -*- coding: utf-8 -*-

import requests
# 未添加cookie访问页面的情况
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'}
if __name__ == '__main__':
    url = 'http://www.renren.com/969119247/profile'
    response = requests.get(url,headers = headers )
    # 将返回的数据保存在html文件里，比起打印在命令行便于查看
    # 我们访问的是个人主页的信息，但由于没有添加cookie他返回的是登录信息页面
    with open('renren.html','w') as f:
        f.write(response.content)