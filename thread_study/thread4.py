# -*- coding: UTF-8 -*-
from time import sleep, ctime
import threading
#多线程共享全局变量：如果不加锁会把数据弄脏
# 但是这样的与串行执行就没什么区别了
#锁机制,创建锁
glock = threading.Lock()


VALUE = 0

def add_value():
    global VALUE

    # 锁起来以后，其他线程再来这个地方以后，他就进不来了，在外面进行等待

    for x in range(100000):
        glock.acquire()  # 上锁
        VALUE+=1
        glock.release()#解锁

    # print ('VALUE:%s\n'%VALUE)

def run():
    # 留意这种线程的启动方式也是可以的
    for t in range(2):
        t = threading.Thread(target=add_value)
        t.start()

    import time
    time.sleep(1)
    print ('VALUE:%s\n' % VALUE)
if __name__ == '__main__':

    run()