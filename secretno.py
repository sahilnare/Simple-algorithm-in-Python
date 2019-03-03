# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:51:22 2019

@author: Sahil
"""
low=0
high=100
avg=(low+high)/2
print("Please think of a number between 0 and 100!")
while 1:
    print("Is your secret number ",str(avg)+' ?')
    suggest=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n")
    if suggest=='h':
        high=avg
    elif suggest=='l':
        low=avg
    elif suggest=='c':
        print("GameOver. Your Secret number was: "+str(avg))
        break
    else:
        print("Sorry wrong input")
    avg=int((low+high)/2)
    
    