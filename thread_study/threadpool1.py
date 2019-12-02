# -*- coding: UTF-8 -*-
# 线程池 高级版
# as_completed 是一个生成器，只会返回已经完成的future
from concurrent.futures import ThreadPoolExecutor,as_completed
from time import sleep
import threading
def get_html(times):
    sleep(int(times))
    print('get page : %s '%times)
    return times


if __name__ == '__main__':

    #实例化一个线程池
    executor = ThreadPoolExecutor(max_workers=4)

    # 批量提交
    urls = [3, 2, 4,10,15,20]

    # 方法一：通过 as_completed 获取已经完成的task
    all_task = []
    for url in urls:
        tmptask = executor.submit(get_html,(url))
        all_task.append(tmptask)

    for future in as_completed(all_task):
        data = future.result()
        print('get page success: %s ' %data)
        print(threading.enumerate())

    # 方法二：通过 executor 获取已经完成的task的值
    # for data in executor.map(get_html, urls):
    #
    #     print('get page success: %s ' %data)





























