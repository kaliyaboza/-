# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:14:02 2023

@author: 陈亚偲2300011106
"""

string1=input().lower()
string2=input().lower()
groud=[string1,string2]
groud.sort()
if string1==string2:
    print(0)
elif groud[1]==string1:
    print(1)
else:
    print(-1)