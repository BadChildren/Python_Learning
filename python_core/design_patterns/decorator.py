#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/21 14:41
# @Author  : xudandan
# @Site    : 装饰模式（动态地为对象增加额外的职责）
# @File    : decorator.py
# @Software: PyCharm

class Person:
    def __init__(self, tname):
        self.name = tname
    def Show(self):
        print "dressed %s " % (self.name)

class Finery(Person):
    component = None
    def __init__(self):
        pass
    def Decorate(self, ct):
        self.component = ct
    def Show(self):
        if(self.component != None):
            self.component.Show()

class Tshirts(Finery):
    def __init__(self):
        pass
    def Show(self):
        print "Big T-shirt "
        self.component.Show()

class BigTrouser(Finery):
    def __init__(self):
        pass
    def Show(self):
        print "Big Trouser "
        self.component.Show()

if __name__ == "__main__":
    p = Person("somebody")
    bt = BigTrouser()
    ts = Tshirts()
    bt.Decorate(p)
    ts.Decorate(bt)
    ts.Show()
