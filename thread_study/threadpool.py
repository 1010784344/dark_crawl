# -*- coding: UTF-8 -*-
# 线程池 初级版
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def get_html(times):
    sleep(int(times))
    print('get page : %s '%times)
    return times


if __name__ == '__main__':
    #实例化一个线程池
    # max_workers：同时运行线程多少个
    executor = ThreadPoolExecutor(max_workers=1)
    # 通过submit 函数提交执行函数到线程池中
    task1 = executor.submit(get_html, (3))
    task2 = executor.submit(get_html,(2))
    # submit 提交上去之后 他就立马得到返回，他是非阻塞的

# 返回的是future 类对象，有一个方法 done：用于判定某个任务是否完成

#  根据返回值可以判断执行状态，有没有执行成功
    print(task1.done())
    # 取消某一个线程任务，取消成功返回 True。但是线程任务执行中，执行完成是取消不了的
    print(task2.cancel())

    sleep(3)

    print(task1.done())
    # result 是一个阻塞的方法，可以得到函数的返回结果
    print(task1.result())