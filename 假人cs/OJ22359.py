# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:23:13 2024

@author: 陈亚偲2300011106
"""
def boza(n):
    ans=[0]*2+[1]*(n-1)
    kk=set()
    for i in range(2,n+1):
        if ans[i]==0:
            continue
        else:
            kk.add(i)
            for j in range(2*i,n+1,i):
                ans[j]=0
    return kk
a=int(input())
ww=boza(a)
for i in ww:
    if a-i in ww:
        print(str(i)+' '+str(a-i))
        break
    
        
