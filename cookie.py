# -*- coding: utf-8 -*-
# cookie 添加到 header 里面进行访问
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36',
           'Cookie':'anonymid=jpnth5w18l1fhj; depovince=GW; _r01_=1; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; JSESSIONID=abcbMYT1ubsXDbV9Se6Ew; ick_login=ad331f30-f7ce-4241-bc72-ad9c6b5eac48; t=d3f4f4c49042ae6faf497d56e0dc3b567; societyguester=d3f4f4c49042ae6faf497d56e0dc3b567; id=969119247; xnsid=45ecf75d; jebecookies=e7ec025e-e66c-4f50-954b-acfe8faf148a|||||; ch_id=10016; wp_fold=0'}

if __name__ == '__main__':
    url = 'http://www.renren.com/969119247/profile'
    response = requests.get(url,headers = headers )
    # 将返回的数据保存在html文件里，比起打印在命令行便于查看
    # 访问个人主页信息
    with open('renren.html','w') as f:
        f.write(response.content)