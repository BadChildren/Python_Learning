#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/22 16:39
# @Author  : xudandan
# @Site    : 原型模式（用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象）
# @File    : Prototype.py
# @Software: PyCharm

import copy

class WorkExp:
    place = ""
    year = 0

class Resume:
    name = ""
    age = 0
    def __init__(self, name):
        self.name = name
    def SetAge(self, age):
        self.age = age
    def SetWorkExp(self, p, y):
        self.place = p
        self.year = y
    def Display(self):
        print self.name
        print self.age
        print self.place
        print self.year
    def Clone(self):
        # 实际不是克隆，只是返回本身
        return self

if __name__ == "__main__":
    a = Resume("a")
    b = a.Clone()
    # print b, type(b)
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a.SetAge(7)
    b.SetAge(12)
    c.SetAge(15)
    d.SetAge(16)
    a.SetWorkExp("PrimarySchool",1996)
    b.SetWorkExp("MidSchool",2001)
    c.SetWorkExp("HighSchool",2004)
    d.SetWorkExp("University",2007)
    a.Display()
    b.Display()
    c.Display()
    d.Display()