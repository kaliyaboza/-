# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:24:41 2023

@author: 陈亚偲2300011106
"""
a=int(input())
b=0
for i in range(a):
    c=input()
    if c=="++X" or c=='X++':
        b=b+1
    elif c=="--X" or c=='X--':
        b=b-1
    else:
        print("不讲武德")
print(b)

