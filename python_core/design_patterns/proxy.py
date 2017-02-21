#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/21 15:17
# @Author  : xudandan
# @Site    : 为其他对象提供一种代理以控制对这个对象的访问
# @File    : proxy.py
# @Software: PyCharm

class Interface:
    def Request(self):
        return 0

class RealSubject(Interface):
    def Request(self):
        print "Real request"

class Proxy(Interface):
    def Request(self):
        self.real = RealSubject()
        self.real.Request()

if __name__ == "__main__":
    p = Proxy()
    p.Request()

