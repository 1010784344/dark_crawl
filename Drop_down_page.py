# -*- coding: UTF-8 -*-

# selenium  爬虫解决下拉分页解决办法
# 执行js脚本
def scroll(driver):
    driver.execute_script(""" 
        (function () { 
            document.getElementsByClassName('scroll-bar-indicator scroll-bar-fade-out')[0].style.transform = 'translate3d(0px, 100px, 0px) scaleY(1)'
            
        })(); 
        """)


from selenium import webdriver
import time
from lxml import etree
if __name__ == '__main__':

    driver_path = r'D:\tools\chromedriver.exe'

    driver = webdriver.Chrome(executable_path=driver_path)

    # 加载界面
    driver.get("https://ai.ofweek.com/")
    time.sleep(3)

    # 逐渐滚动浏览器窗口，令ajax逐渐加载
    for i in range(0, 100):

        # 方法一：竖向滚动条置底（操作滚动条）
        # 执行js脚本
        # driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # i += 1

        # 方法二：做元素定位时，有的元素在页面的不可见区域，这时候需要scrollIntoView()将其拖动到可见区域
        target = driver.find_elements_by_xpath("//span[@class='more-wenzi']")[0]

        driver.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(1)

        #方法三：函数执行js脚本
        # scroll(driver)

    # 拿到页面源码
    html = driver.page_source
    print(html)


