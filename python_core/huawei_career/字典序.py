#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/11 16:05
# @Author  : xudandan
# @Site    : 
# @File    : 字典序.py
# @Software: PyCharm

if __name__ == '__main__':
    num = input()
    str_list = []
    for i in range(num):
        string = raw_input()
        str_list.append(string)
    str_list = sorted(str_list)
    for val in str_list:
        print val