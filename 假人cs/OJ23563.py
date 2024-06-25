# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 19:28:04 2023

@author: 陈亚偲2300011106
"""
a=input().split('+')
b=[]
for j in a:
    i=j.split('n^')
    if i[0]!='0':
        b.append(int(i[1]))
print('n^'+str(max(b)))

