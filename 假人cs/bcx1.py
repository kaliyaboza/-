# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:43:15 2023

@author: abrac
"""

def checkAt(address):
    cnt = 0
    for i in address:
        if i == '@':
            cnt += 1
            
    return cnt == 1

def checkHeadAndTail(address):
    check = False if address[0] == '.' or address[-1] == '.' or address[0] == '@' or address[-1] == '@' else True
    return check
    
def checkAtAndDot(address):
    cnt, pos = 0, 0
    for i in range(len(address)):
        if address[i] == '@':
            pos = i
            if address[pos - 1] == '.' or address[pos + 1] == '.':
                return False
    for i in range(pos, len(address)):
        if address[i] == '.':
            cnt += 1
    
    return cnt > 0

def check(address):
    return checkAt(address) and checkHeadAndTail(address) and checkAtAndDot(address)

while True:
    try:
        print('YES' if check(input()) else 'NO')
    except EOFError:
        break