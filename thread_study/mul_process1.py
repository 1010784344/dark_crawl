# -*- coding: UTF-8 -*-
import multiprocessing
import time

def get_html(n):
    time.sleep(n)
    print 'sub_process success'
    return n

if __name__ == '__main__':
    process = multiprocessing.Process(target=get_html, args=(2,))
    process.start()
    # 打印进程id
    print process.pid
    process.join()
    print 'main_process success'
