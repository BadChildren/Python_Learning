#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/11 14:35
# @Author  : xudandan
# @Site    : 桥接模式（将抽象部分与它的实现部分分离，使它们都可以独立地变化）
# @File    : bridge.py
# @Software: PyCharm

class HandsetSoft(object):
    def Run(self):
        pass

class HandsetGame(HandsetSoft):
    def Run(self):
        print "Game"

class HandsetAddressList(HandsetSoft):
    def Run(self):
        print "Address List"

class HandsetBrand(object):
    def __init__(self):
        self.m_soft = None
    def SetHandsetSoft(self,temp):
        self.m_soft= temp
    def Run(self):
        pass

class HandsetBrandM(HandsetBrand):
    def Run(self):
        if not (self.m_soft == None):
            print "BrandM"
            self.m_soft.Run()

class HandsetBrandN(HandsetBrand):
    def Run(self):
        if not (self.m_soft == None):
            print "BrandN"
            self.m_soft.Run()

if __name__ == "__main__":
    brand = HandsetBrandM()
    brand.SetHandsetSoft(HandsetGame())
    brand.Run()
    brand.SetHandsetSoft(HandsetAddressList())
    brand.Run()