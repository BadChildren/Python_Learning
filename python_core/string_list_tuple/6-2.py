#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import keyword

def judge(stringA, stringB, length):
    if stringA in keyword.kwlist:
        print('是关键字')
    else:
        print('不是关键字')
    if len(stringA) == length:
        if stringA in stringB:
            return True
        else:
            return False
    else:
        print('不能判断该长度的字符串')


if __name__ ==  '__main__':
    # print(keyword.kwlist)
    stringA = input()
    stringB = input()
    print  (judge(stringA, stringB, 5))