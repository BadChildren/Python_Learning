#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/11 14:45
# @Author  : xudandan
# @Site    : 命令模式（将请求封装成对象，从而使可用不同的请求对客户进行参数化；对请求排队或记录请求日志，以及支持可撤消的操作。）
# @File    : command.py
# @Software: PyCharm

class Barbucer:
    def MakeMutton(self):
        print "Mutton"

    def MakeChickenWing(self):
        print "Chicken Wing"


class Command:
    def __init__(self, temp):
        self.receiver = temp

    def ExecuteCmd(self):
        pass


class BakeMuttonCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeMutton()


class ChickenWingCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeChickenWing()


class Waiter:
    def __init__(self):
        self.order = []

    def SetCmd(self, command):
        self.order.append(command)
        print "Add Order"

    def Notify(self):
        for cmd in self.order:
            # self.order.remove(cmd)
            # lead to a bug
            cmd.ExecuteCmd()


if __name__ == "__main__":
    barbucer = Barbucer()
    cmd = BakeMuttonCmd(barbucer)
    cmd2 = ChickenWingCmd(barbucer)
    girl = Waiter()
    girl.SetCmd(cmd)
    girl.SetCmd(cmd2)
    girl.Notify()