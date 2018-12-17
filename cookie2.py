# -*- coding: utf-8 -*-

import requests
# 未添加cookie访问页面的情况
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'}
cookie='anonymid=jpnth5w18l1fhj; depovince=GW; _r01_=1; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; JSESSIONID=abcbMYT1ubsXDbV9Se6Ew; ick_login=ad331f30-f7ce-4241-bc72-ad9c6b5eac48; t=d3f4f4c49042ae6faf497d56e0dc3b567; societyguester=d3f4f4c49042ae6faf497d56e0dc3b567; id=969119247; xnsid=45ecf75d; jebecookies=e7ec025e-e66c-4f50-954b-acfe8faf148a|||||; ch_id=10016; wp_fold=0'


if __name__ == '__main__':
    url = 'http://www.renren.com/969119247/profile'
    cookie_dict = {i.split('=')[0] : i.split('=')[1] for i in cookie.split('; ')}
    # cookie 字典传给cookies 参数
    response = requests.get(url,headers = headers,cookies = cookie_dict )

    with open('renren2.html','w') as f:
        f.write(response.content)