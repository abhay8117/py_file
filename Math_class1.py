# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:38:14 2020

@author: SONY
"""

class math:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #self.lx=len(x)
        #self.ly=len(y)
        
    def addition(self,x,y):
        if len(self.x)>1:
            t=[]
            for i in range(self.x):
                s=self.x[i]+self.y[i]
                t.append(s)
        else:
            t=self.x+self.y
        return t
        
    def subtraction(self,x,y):
        if len(self.x)>1:
            t=[]
            for i in range(self.x):
                s=self.x[i]-self.y[i]
                t.append(s)
        else:
            t=self.x-self.y
        return t
        
        
    def multipication(self,x,y):
        if len(self.x)>1:
            t=[]
            for i in range(self.x):
                s=self.x[i]*self.y[i]
                t.append(s)
        else:
            t=self.x*self.y
        return t
        
    def division(self,x,y):
        if len(self.x)>1:
            t=[]
            for i in range(self.x):
                s=self.x[i]/self.y[i]
                t.append(s)
        else:
            t=self.x/self.y
        return t
        
