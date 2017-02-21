#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/21 16:27
# @Author  : xudandan
# @Site    : 工厂方法模式（基类雷锋类，派生出学生类和志愿者类，由这两种子类完成“学雷锋”工作。
#                           子类的创建由雷锋工厂的对应的子类完成）
# @File    : factory_function.py
# @Software: PyCharm

class LeiFeng:
    def Sweep(self):
        print "LeiFeng sweep"

class Student(LeiFeng):
    def Sweep(self):
        print "Student sweep"

class Volunter(LeiFeng):
    def Sweep(self):
        print "Volunter sweep"

class LeiFengFactory:
    def CreateLeiFeng(self):
        temp = LeiFeng()
        return temp

class StudentFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Student()
        return temp

class VolunterFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Volunter()
        return temp

if __name__ == "__main__":
    sf = StudentFactory()
    s = sf.CreateLeiFeng()
    s.Sweep()
    sdf = VolunterFactory()
    sd = sdf.CreateLeiFeng()
    sd.Sweep()