#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/10 17:26
# @Author  : xudandan
# @Site    : 
# @File    : 质数因子.py
# @Software: PyCharm

import math

# def prime(num):
#     temp = int(math.sqrt(num)) + 1
#     for i in range(2,temp):
#         # print i
#         if num % i == 0:
#             return 0
#     return 1

if __name__ == '__main__':
    num = input()
    res = []
    for i in range(2,num+1):
        while num % i == 0:
            res.append(i)
            num /= i
    str_res = ''
    for i in range(len(res)):
        str_res += str(res[i]) + ' '
    print str_res

# if __name__ == '__main__':
#     num = input()
#     res = {}
#     for i in range(num):
#         index,value = map(int, raw_input().split())
#         if res.has_key(index):
#             res[index] += value
#         else:
#             res[index] = value
#     for k,v in res.items():
#         print k, v


# if __name__ == '__main__':
#     num = raw_input()
#     num_str = str(num)[::-1]
#     res = ''
#     judge = set()
#     for i in range(len(num_str)):
#         if num_str[i] not in judge:
#             res += num_str[i]
#             judge.add(num_str[i])
#     print int(res)
