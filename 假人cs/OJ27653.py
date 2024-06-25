# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:28:03 2024

@author: 陈亚偲 2300011106
"""
def daza(n):
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
class boza:
    def __init__(self,zi,mu):
        self.zi=zi
        self.mu=mu
        self.num=zi/mu
    def cyc(self):
        return str(self.zi)+'/'+str(self.mu)
def add(a,b,c,d):
    def ciza(k,m):
        mm=min([k,m])
        da=daza(mm)
        for i in da:
            while k%i==0 and m%i==0:
                k=k//i
                m=m//i
        return [k,m]
    return ciza(a*d+b*c,b*d)
a,b,c,d=map(int,input().split())
m,n=add(a,b,c,d)[0],add(a,b,c,d)[1]
eza=boza(m,n)
print(eza.cyc())

    