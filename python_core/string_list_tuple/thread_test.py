#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/10 下午3:53
# @Author  : xudandan 
# @Site    : 
# @File    : thread_test.py
# @Software: PyCharm

import thread
from time import sleep, ctime

def loop0():
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'loop o done at:', ctime()

def loop1():
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 done at :', ctime()

def fun1():
    print 'startting at:', ctime()
    loop0()
    loop1()
    print 'all done at:', ctime()

def fun2():
    print 'startting at:', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all done at:', ctime()

if __name__ == '__main__':
    fun1()
    fun2()
