# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:27:36 2023

@author: 陈亚偲2300011106
"""
sum1=[int(i) for i in input().split('+')]
sum1.sort()
a=len(sum1)
sum2=str(sum1[0])
for i in range(1,a):
    sum2=sum2 + '+' + str(sum1[i])
print(sum2)
