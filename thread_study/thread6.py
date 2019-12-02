# -*- coding: UTF-8 -*-
# 未使用锁结果不准确
import threading


VALUE = 0

def add_value():

    global VALUE

    for x in range(100000):

        VALUE += 1

    print ('VALUE:%s\n'%VALUE)

def run1():
    # 使用run1运行结果还是正确的，是因为join的是使用，join 的作用是使主线程等待子线程的运行完毕再运行主线程，
    # 现在这种用法是先开了一个子线程然后 join，其实就在阻塞等待子线程的运行完毕才运行主线程，然后才继续循环开启另一个线程
    # 这种写法 就相当于没有开启线程
    for t in range(2):
        t = threading.Thread(target=add_value)
        t.start()
        t.join()


def run2():
    t1 = threading.Thread(target=add_value)
    t2 = threading.Thread(target=add_value)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    # 使用run1运行结果还是正确的
    # run1()

    # 使用run2运行结果会不准确
    run2()