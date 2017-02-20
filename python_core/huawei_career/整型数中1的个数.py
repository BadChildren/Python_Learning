#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/11 16:23
# @Author  : xudandan
# @Site    : 
# @File    : 整型数中1的个数.py
# @Software: PyCharm

if __name__ == '__main__':
    num = input()
    count = 0
    while num:
        num = num & (num-1)
        count += 1
    print count