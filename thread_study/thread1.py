# -*- coding: UTF-8 -*-
from time import sleep, ctime
# 无线程参与
def code():
    for x in range(3):
        print '正在code：%s'%x
        sleep(1)

def draw():
    for x in range(3):
        print '正在draw：%s'%x
        sleep(1)

def run():
    code()
    draw()

if __name__ == '__main__':
    print 'Start playing： %s' % ctime()
    run()
    print 'end:%s' % ctime()