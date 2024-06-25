# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:14:28 2023

@author: 陈亚偲2300011106
"""
A=[]
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    a=[int(i) for i in input().split()]
    ct=True
    for apple in a:
        if apple % y != 0:
            ct=False
    if ct:
        A.append(-1)
    elif (sum(a))%y!=0:
        A.append(x)
    else:
        for i in range(x//2+1):
            if a[i] % y!=0 or a[x-i-1] %y!=0:
                A.append(x-i-1)
                break
for i in A:
    print(i)
        
            