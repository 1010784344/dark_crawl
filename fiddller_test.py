# -*- coding: utf-8 -*-
import requests
# 利用 fiddler 抓包工具，查看接口，访问应用宝里面的数据交互

requests.packages.urllib3.disable_warnings()
if __name__ == '__main__':
    url = 'https://m5.qq.com/pcsoftmgr/searchapp.htm?keyword=%25E7%25B2%2589%25E4%25B8%259D%25E7%25BD%2591&searchScene=1&pageSize=20'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 QBCore/3.43.815.400 QQBrowser/9.0.2524.400'
,'X-Requested-With':'XMLHttpRequest',
'Accept-Encoding':'gzip, deflate',
'Accept':'*/*',
'Accept-Language':'en-US,en;q=0.8',
'Referer':'https://m5.qq.com/app/new/'
,'Host':'m5.qq.com',
'Connection':'keep-alive'}

    response = requests.get(url,verify=False)


    print response.content














