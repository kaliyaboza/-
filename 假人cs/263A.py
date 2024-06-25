# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:17:30 2023

@author: 陈亚偲2300011106
"""
line1=[int(i) for i in input().split()]
line2=[int(i) for i in input().split()]
line3=[int(i) for i in input().split()]
line4=[int(i) for i in input().split()]
line5=[int(i) for i in input().split()]
for i in range(5):
    if line1[i]!=0:
        print(abs(i-2)+2)
        
for i in range(5):
    if line2[i]!=0:
        print(abs(i-2)+1)
        
for i in range(5):
    if line3[i]!=0:
        print(abs(i-2))
        
for i in range(5):
    if line4[i]!=0:
        print(abs(i-2)+1)
        
for i in range(5):
    if line5[i]!=0:
        print(abs(i-2)+2)
