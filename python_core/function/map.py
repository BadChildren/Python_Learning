#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def map(func, seq):
    mapped_seq = []
    for eachItem in seq:
        mapped_seq.append(func(eachItem))
    return mapped_seq

print( map((lambda x: x+2), [0,1,2,3,4,5]) )
# 等价于
print( [x+2 for x in range(6)] )

print( map(lambda x:x**2, range(6)) )

# 等价于
print( [x**2 for x in range(6)] )

print( map(lambda x,y: x+y, [1,3,5], [2,4,6]))

print( map(lambda x,y:(x+y, x-y), [1,3,5], [2,4,6]))

print( map(None, [1,3,5], [2,4,6]))
