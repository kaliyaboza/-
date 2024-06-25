# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:02:53 2023

@author: abrac
"""

index, s = 0, 'hello '
for c in input():
    if c == s[index]:
        index += 1
print('YES' if index == 5 else 'NO')