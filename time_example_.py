# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:05:47 2019

@author: SONY
"""

#
import time

filename='table1.txt'
f=open(filename,'r')
chunk_size=300_000
f1=f.read(chunk_size)
counter=1
t1=time.perf_counter()
while len(f1)>0:
    f1=f.read(chunk_size)
    counter+=1
    
f.close()
t2=time.perf_counter()
t=t2-t1
print('Execution=',t)