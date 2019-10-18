# -*- coding: UTF-8 -*-
# selenium 完整流程
# 主页列表加详情页信息爬取

from selenium import webdriver
from lxml import etree
import time

class lagouSpider(object):
    driver_path = r'D:\tools\chromedriver.exe'
    def __init__(self):
        # 注意 driver_path 的引用
        self.driver = webdriver.Chrome(executable_path=lagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.posiav = []

        # 解析对应的详情页
    def request_detail_page(self, table):
        self.driver.get(table)
        data = self.driver.page_source

        htmlstr = etree.HTML(data)

        advantage = htmlstr.xpath('//dd[@class="job-advantage"]/p/text()')

        advantagedict = {u'职位诱惑': advantage}

        print advantagedict

        self.posiav.append(advantagedict)

    # 解析主页
    def run(self):

        self.driver.get(self.url)
        # 一直循环，直到最后一页退出
        while True:

            source = self.driver.page_source
            #解析每个url
            self.parse_list_page(source)

            # 选中主页元素 点击执行下一页
            nextTag = self.driver.find_elements_by_xpath('//span[@action="next"]')[0]
            # 如果class有‘pager_next pager_next_disabled’这个属性就结束
            if 'pager_next pager_next_disabled' in nextTag.get_attribute('class'):
                break
            else:
                nextTag.click()
            time.sleep(2)

    def parse_list_page(self,source):

        # 给详情页单独新建一个窗口
        self.driver.execute_script('window.open("%s")' % self.url)
        self.driver.switch_to_window(self.driver.window_handles[1])

        htmlobj = etree.HTML(source)
        # <a class="position_link" href="https://www.lagou.com/jobs/4694651.html"</a>
        for table in htmlobj.xpath('//a[@class="position_link"]/@href'):
            # 控制爬取的频率
            time.sleep(1)

            self.request_detail_page(table)

        #关闭详情页窗口
        self.driver.close()
        # 并切换回主页
        self.driver.switch_to_window(self.driver.window_handles[0])




if __name__ == '__main__':
    lagou = lagouSpider()
    lagou.run()