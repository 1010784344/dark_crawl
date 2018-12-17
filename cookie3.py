# -*- coding: utf-8 -*-
import requests
# 此url特指登录页面form/action 属性的登录链接
url = 'http://www.renren.com/PLogin.do'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'}
postdata = {'email':'18735934287','password':'cwx364505'}


if __name__ == '__main__':
    # 实例化session
    session = requests.session()
    # 使用session发送post请求，获取对方保存在本地的cookie
    session.post(url,headers=headers,data=postdata)

    # 在使用session，请求登录后的页面
    my_url = 'http://www.renren.com/969150381/profile'
    response = session.get(my_url,headers=headers)
    with open('renren3.html','w') as f:
        f.write(response.content)
