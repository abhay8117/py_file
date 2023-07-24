# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:23:04 2019

@author: SONY
"""

import math
pi=math.pi
t1=pi**2+math.sin(pi)-10
print(t1)
t2=3**2+math.sin(3)-10
print(t2)

x=2
t=x**2+math.sin(x)-10


def simplemaths(x):
    x=pi
    t3=x**2+math.sin(x)-10
    return t3
print(simplemaths(45))
list_array=[4,5,6,7,8]
output=[]
for x in list_array:
    out=simplemaths(x)
    output.append(out)
    
