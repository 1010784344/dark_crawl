# -*- coding: UTF-8 -*-
from time import sleep, ctime
import threading
# 传统写法:有线程参与
def code():
    for x in range(3):
        print '正在code：%s' % x
        # 打印当前线程的名字
        print threading.current_thread()
        sleep(1)


def draw():
    for x in range(3):
        print '正在draw：%s' % x
        sleep(1)


def run():
    # 不传 code() 的原因，意味着你是把函数的返回值赋值给target，因为我们是将函数的本身赋值给target，
    t1 = threading.Thread(target=code)
    t2 = threading.Thread(target=draw)
    t1.start()
    t2.start()

    # 查看当前的线程数
    print threading.enumerate()

    t1.join()
    t2.join()
if __name__ == '__main__':
    print 'Start playing： %s' % ctime()
    run()
    print 'end:%s' % ctime()