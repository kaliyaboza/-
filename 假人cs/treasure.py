# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 00:00:22 2023

@author: 陈亚偲2300011106
"""
dt={' ':0,'X':2}
ans=[]
p=[0,1,0,-1]
q=[-1,0,1,0]
while True:
    m,n=map(int,input().split())
    if n==0 and m==0:
        break
    w=[]
    l=[[2]*(m+2)]
    for i in range(n):
        l.append([2]+[dt[j] for j in list(input())]+[2])
    l.append([2]*(m+2))
    while True:
        a=[]
        for i in range(n+2):
            a.append(l[i][:])
        x,y,z,s=map(int,input().split())
        if x==0:
            break
        a[y][x]=3
        a[s][z]=1
        ct=0
        boza=True
        ciza=True
        while boza and ciza:
            ciza=False
            ct+=1
            for i in range(1,n+1):
                if not boza:
                    break
                for j in range(1,m+1):
                    if not boza:
                        break
                    if a[i][j]==3:
                        a[i][j]=4
                        for k in range(4):
                            if a[i+p[k]][j+q[k]]==1:
                                boza=False
                                break
                            elif a[i+p[k]][j+q[k]]==0:
                                a[i+p[k]][j+q[k]]=5
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if a[i][j]==5:
                        a[i][j]=3
                        ciza=True
        if boza:
            w.append('impossible.')
        else:
            w.append(str(ct)+' segments.')
    ans.append(w)
for i in range(len(ans)):
    print('Board #'+str(i+1)+':')
    for j in range(len(ans[i])):
        print('Pair '+str(j+1)+': '+ans[i][j])
                  
