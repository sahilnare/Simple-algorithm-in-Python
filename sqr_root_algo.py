# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:41:19 2019

@author: Sahil
"""

num = int(input("Enter a number: "))
low = 1
high = num
avr = (high + low)/2
accu = 0.000001
guess = 0
while abs(avr**2 - num) >= accu:
    if avr**2 > num:
        high = avr
    else:
        low = avr
    avr = (high + low)/2
    guess += 1
print("Answer is: " + str(avr))
print("No of guesses taken: " + str(guess))