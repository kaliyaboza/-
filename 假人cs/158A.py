# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:18:30 2023

@author: 陈亚偲2300011106
"""
people=input()
score=input()
p_p=people.split()
s_c=score.split()
PP=[int(i) for i in p_p]
SC=[int(i) for i in s_c]
num_all=PP[0] #总人数
good=PP[1] #晋级人数
if SC[0]==0:
    print(0)
else:
    deadline=SC[good-1]
    for i in range(num_all):
        if SC[-1]<deadline:
            del SC[-1]
    while 0 in SC:
        del SC[-1]
    print(len(SC))
