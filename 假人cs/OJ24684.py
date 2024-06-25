# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:46:15 2024

@author: 陈亚偲2300011106
"""
ans=[]
from collections import defaultdict
a=defaultdict(int)
w=[int(i) for i in input().split()]
for i in w :
    a[i]+=1
kk=max(a.values())
for i in a.keys():
    if a[i]==kk:
        ans.append(i)
print(*sorted(ans))
    



