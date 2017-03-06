#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/1 16:02
# @Author  : xudandan
# @Site    : 适配器模式（将一个类的接口转换成为客户希望的另外一个接口）
# @File    : adapter.py
# @Software: PyCharm

class Target:
    def Request():
        print "common request."

class Adaptee(Target):
    def SpecificRequest(self):
        print "specific request."

class Adapter(Target):
    def __init__(self,ada):
        self.adaptee = ada
    def Request(self):
        self.adaptee.SpecificRequest()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.Request()