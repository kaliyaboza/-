# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:17:55 2024

@author: 陈亚偲2300011106
"""
a=input()
b="hello"
index=0
haha=0
while index<=4 and haha<len(a):
    if a[haha]==b[index]:
        index+=1
    haha+=1
if index==5:
    print('YES')
else:
    print('NO')

