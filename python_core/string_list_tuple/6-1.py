#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def judge(stringA,stringB):
    if stringA in stringB:
        return True
    else:
        return False


if __name__ ==  '__main__':
    stringA = input()
    stringB = input()
    print  (judge(stringA, stringB))
