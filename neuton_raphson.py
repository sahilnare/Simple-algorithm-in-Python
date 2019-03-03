# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:31:29 2019

@author: Sahil
"""

acc=0.001
num=int(input('Enter a number: '))
numcount=0
a = int(input('Enter the nth root: '))
guess=num/2
while abs((guess**a)-num) >= acc:
    numcount+=1
    guess=guess-((guess**a-num)/(a*(guess**(a-1))))
    
print('No of guesses taken: ' + str(numcount))
print('The square root is: ' + str(guess))