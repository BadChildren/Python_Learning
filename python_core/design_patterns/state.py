#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/1 15:54
# @Author  : xudandan
# @Site    : 状态模式（当一个对象的内在状态改变时允许改变其行为，这个对象看起来像是改变了其类）
# @File    : state.py
# @Software: PyCharm

class State:
    def WirteProgram(self):
        pass

class Work:
    def __init__(self):
        self.hour = 9
        self.current = ForenoonState()
    def SetState(self,temp):
        self.current = temp
    def WriteProgram(self):
        self.current.WriteProgram(self)

class NoonState(State):
    def WriteProgram(self,w):
        print "noon working"
        if (w.hour<13):
            print "fun."
        else:
            print "need to rest."

class ForenoonState(State):
    def WriteProgram(self,w):
        if (w.hour<12):
            print "morning working"
            print "energetic"
        else:
            w.SetState(NoonState())
            w.WriteProgram()

if __name__ == "__main__":
    mywork = Work()
    mywork.hour = 9
    mywork.WriteProgram()
    mywork.hour =14
    mywork.WriteProgram()
