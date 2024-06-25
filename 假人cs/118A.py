# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:04:33 2023

@author: 陈亚偲2300011106
"""
a=list(input().lower())
for apple in ['a','e','i','o','u','y']:
    while apple in a:
        a.remove(apple)
for i in range(len(a)):
    a.insert(2*i,'.')
print(''.join(a))



