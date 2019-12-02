# -*- coding: UTF-8 -*-
# web 库存不一致模型
import threading

total = 0

def add():
    global total
    for i in range(1000000):
        total = total + 1

def desc():
    global total
    for i in range(1000000):
        total = total - 1


if __name__ == '__main__':
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print total
