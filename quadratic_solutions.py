# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:33:57 2019

@author: Sahil
"""
import math
def root1(x,y,z):
    return (-y + math.sqrt(y**2 - 4*x*z))/(2*x)
def root2(x,y,z):
    return (-y - math.sqrt(y**2 - 4*x*z))/(2*x)
def img1(x,y,z):
    return math.sqrt(-(y**2 - 4*x*z))/(2*x)
def img2(x,y,z):
    return -math.sqrt(-(y**2 - 4*x*z))/(2*x)

a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))

if (b**2 - 4*a*c) < 0:
    print('The roots are imaginary')
    rti1 = img1(a,b,c)
    rti2 = img2(a,b,c)
    rti = -b/(2*a)
    print('The roots are: ' + str(rti) + ' + ' + str(rti1) + 'i' + ' and ' + str(rti) + ' + ' + str(rti2) + 'i')
else:
    print('The roots are real')
    rtr1 = root1(a,b,c)
    rtr2 = root2(a,b,c)
    print('The roots are: ' + str(rtr1) + ' and ' + str(rtr2))

print('Thank you')