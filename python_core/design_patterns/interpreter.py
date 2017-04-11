#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/11 14:53
# @Author  : xudandan
# @Site    : 解释器模式（给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子）
# @File    : interpreter.py
# @Software: PyCharm

class Context:
    def __init__(self):
        self.input=""
        self.output=""

class AbstractExpression:
    def Interpret(self,context):
        pass

class Expression(AbstractExpression):
    def Interpret(self,context):
        print "terminal interpret"

class NonterminalExpression(AbstractExpression):
    def Interpret(self,context):
        print "Nonterminal interpret"

if __name__ == "__main__":
    context= ""
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)