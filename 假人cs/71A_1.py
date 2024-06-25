# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:06:40 2023

@author: 陈亚偲2300011106
"""

n=int(input())
word = [''] * n
for i in range(n):
    word[i]=input()
for i in range(n):
    if len(word[i]) >=11 :
        print( word[i][0] + str(len(word[i])-2)+ word[i][-1] )
    else:
        print(word[i])