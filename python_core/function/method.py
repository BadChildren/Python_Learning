#!/usr/bin/env python2.79
# -*- coding: utf-8 -*-

class TestStaticMethod:
    @staticmethod
    def foo():
        print 'calling static method foo()'


class TestClassMethod:
    @classmethod
    def foo(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__

if __name__ == '__main__':
    tsm = TestStaticMethod()
    tsm.foo()
    tcm = TestClassMethod()
    tcm.foo()