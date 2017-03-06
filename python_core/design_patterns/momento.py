#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/1 16:05
# @Author  : xudandan
# @Site    : 备忘录模式（在不破坏封装性的前提下捕获一个对象的内部状态，
#            并在该对象之外保存这个状态，以后可以将对象恢复到这个状态）
# @File    : momento.py
# @Software: PyCharm

class Originator:
    def __init__(self):
        self.state = ""
    def Show(self):
        print self.state
    def CreateMemo(self):
        return Memo(self.state)
    def SetMemo(self,memo):
        self.state = memo.state

class Memo:
    state= ""
    def __init__(self,ts):
        self.state = ts

class Caretaker:
    memo = ""

if __name__ == "__main__":
    on = Originator()
    on.state = "on"
    on.Show()
    c = Caretaker()
    c.memo=on.CreateMemo()
    on.state="off"
    on.Show()
    on.SetMemo(c.memo)
    on.Show()