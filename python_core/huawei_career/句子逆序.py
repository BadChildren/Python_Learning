#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/11 15:48
# @Author  : xudandan
# @Site    : 
# @File    : 句子逆序.py
# @Software: PyCharm

if __name__ == '__main__':
    string = raw_input()
    temp = string.split(' ')
    res = ''
    for val in temp[::-1]:
        res += val
        if val != temp[0]:
            res += ' '
    print res