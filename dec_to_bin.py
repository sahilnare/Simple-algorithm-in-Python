# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:07:17 2019

@author: Sahil
"""

num = int(input("Enter a number please."))
dig = 0
ans = ''
while num > 0:
    dig = num%2
    ans = str(dig) + ans
    num = num//2
print(ans)