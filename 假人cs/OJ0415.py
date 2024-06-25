# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:55:11 2023

@author:陈亚偲2300011106
"""
a=[]
while True:    
    try:
        a.append(input())
    except:
        break
for apple in a:
    rules=[0,0,0]
    email1=list(apple)
    email2=email1[:]#copy
    if '@' in email1:
        email1.remove('@')
        if '@' not in email1:
            rules[0]=1# the first rule
    if email2[0] not in ['@','.'] and email2[-1] not in ['@','.']:
        rules[1]=1# the second rule
    email2.append('我一定会ac的！')#防止out of range，增加自信
    email2.insert(0,'hello world')
    for i in range(len(email2)):
        if email2[i]=='@':
            for j in range(i+1,len(email2)):
                if email2[i+1]!='.' and email2[j] == '.' and email2[i-1]!='.' :
                    rules[2]=1# the third rule
    if 0 in rules:
        print('NO')
    else:
        print('YES')
    

        
    
