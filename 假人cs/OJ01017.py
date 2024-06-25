# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:31:09 2023

@author: 陈亚偲2300011106
"""
a=[]
while True:
    a.append(list(map(int,input().split())))
    if sum(a[-1])==0:
        break
del a[-1]

for b in a:
    b.insert(0,'@')#纯粹为了后面算的简单
    num=b[6] + b[5] + b[4] + (b[3]+3)//4
    if b[3]%4==0:
        box2=b[4]*5
    else:
        box2=b[4]*5 + 2*(4-(b[3]%4))-1
    if b[2]>box2:
        num += ((b[2]-box2)+8)//9
    box1=num*36-b[6]*36-b[5]*25-b[4]*16-b[3]*9-b[2]*4
    if b[1]>box1:
        num += ((b[1]-box1)+35)//36
    print(num)
    
    
