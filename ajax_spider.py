# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
if __name__ == '__main__':
    driver_path = r'D:\tools\chromedriver.exe'
    # 有了driver 以后就可以使用driver去操作浏览器了
    driver = webdriver.Chrome(executable_path=driver_path)

    driver.get('https://www.baidu.com/')
    # 打印网页源代码
    # print driver.page_source
    # time.sleep(5)

    # 根据id查找元素
    # inputTag = driver.find_element_by_id('kw')
    # 根据name查找元素
    # inputTag = driver.find_element_by_name('wd')

    # 根据class查找元素
    inputTag = driver.find_element_by_class_name('s_ipt')
    # 输入数据
    inputTag.send_keys('python')

    btnTag = driver.find_element_by_id('su')
    btnTag.click()
    # driver.close()
    # driver.quit()













