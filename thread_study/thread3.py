# -*- coding: UTF-8 -*-
from time import sleep, ctime
import threading
# threading类的写法:有线程参与

class Code(threading.Thread):
    def run(self):
        for x in range(3):
            print '正在code：%s' % x
            # 打印当前线程的名字
            print threading.current_thread()
            sleep(1)


class Draw(threading.Thread):
    def run(self):
        for x in range(3):
            print '正在draw：%s' % x
            sleep(1)


def run():

    t1 = Code()
    t2 = Draw()
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