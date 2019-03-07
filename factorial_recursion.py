# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:44:56 2019

@author: Sahil
"""

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

num = int(input("Enter a number my friend\n"))
print("The factorial of " + str(num) + " is " + str(fact(num)))
