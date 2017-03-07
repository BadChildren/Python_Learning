#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/1 15:45
# @Author  : xudandan
# @Site    : 抽象工厂模式（提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类）
# @File    : abstract_factory.py
# @Software: PyCharm

class IUser:
    def GetUser(self):
        pass
    def InsertUser(self):
        pass

class IDepartment:
    def GetDepartment(self):
        pass
    def InsertDepartment(self):
        pass

class CAccessUser(IUser):
    def GetUser(self):
        print "Access GetUser"
    def InsertUser(self):
        print "Access InsertUser"


class CAccessDepartment(IDepartment):
    def GetDepartment(self):
        print "Access GetDepartment"
    def InsertDepartment(self):
        print "Access InsertDepartment"

class CSqlUser(IUser):
    def GetUser(self):
        print "Sql GetUser"
    def InsertUser(self):
        print "Sql InsertUser"


class CSqlDepartment(IDepartment):
    def GetDepartment(self):
        print "Sql GetDepartment"
    def InsertDepartment(self):
        print "Sql InsertDepartment"

class IFactory:
    def CreateUser(self):
        pass
    def CreateDepartment(self):
        pass

class AccessFactory(IFactory):
    def CreateUser(self):
        temp=CAccessUser()
        return temp
    def CreateDepartment(self):
        temp = CAccessDepartment()
        return temp

class SqlFactory(IFactory):
    def CreateUser(self):
        temp = CSqlUser()
        return temp
    def CreateDepartment(self):
        temp = CSqlDepartment()
        return temp

if __name__ == "__main__":
    factory = SqlFactory()
    user=factory.CreateUser()
    depart=factory.CreateDepartment()
    user.GetUser()
    depart.GetDepartment()

    factory = AccessFactory()
    user = factory.CreateUser()
    depart = factory.CreateDepartment()
    user.GetUser()
    depart.GetDepartment()