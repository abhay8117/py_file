# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:04:57 2020

@author: SONY
"""

x=[9,4,2,3,5,8,7,6,1,1]
l=len(x)

print(f'Before {x}')
"""mx=x[1]
for i in range(1,l):
    if x[i]>mx:
        mx=x[i]"""
        
for idx in range(l):
    mx=x[idx]
    for idx1 in range(idx,l):
        temp=x[idx1]
        if temp<mx: #asscending order #temp>mx -> decending order
            x[idx1]=mx
            mx=temp
            x[idx]=mx
print(f'After {x}')


#Q1. Write a function to compare two string, equal or not(same).

def Strcompare(str1,str2):
    if str1==str2:
        print('Equal')
    else:
        print('Not equal')


#Q2. Write a user define 

def CheckWord(sentence,word):
    sentence=sentence.lower()
    word=word.lower()
    if word in sentence:
        return 1
    else:
        return 0
    
#if we want access previous output we use _

def Exactword(sentence,word):
    sentence=sentence.lower()
    token=sentence.split(' ')
    word=word.lower()
    if word in token:
        return 1
    else:
        return 0


        

