# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:38:37 2023

@author: 陈亚偲2300011106
"""
n=int(input())
a=[int(i) for i in input().split()]
b=dict()
c=dict()
ans=0
boza=True
for i in range(n):
    if a[i] not in b.keys():
        b[a[i]]=1
        if 1 in c.keys():
            c[1]+=1
        else:
            c[1]=1
    else:
        b[a[i]]+=1
        
        if b[a[i]] in c.keys():
            c[b[a[i]]]+=1
        else:
            c[b[a[i]]]=1
        c[b[a[i]]-1]-=1
        if c[b[a[i]]-1]==0:
            del c[b[a[i]]-1]
    if len(c)<=2:
        if 1 in c.keys():
            if len(c)==1 or c[1]==1:
                boza=True
            
        if len(c)==2:
            p,q=map(int,list(c.keys()))
            if p==q+1 or q==p+1: 
                if c[max(p,q)]==1:
                    boza=True
    if boza:
        ans=i+1
        boza=False
print(ans)

    
    