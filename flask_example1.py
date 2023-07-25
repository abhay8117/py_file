# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 15:54:41 2019

@author: SONY
"""

#write a program to input two 

from flask import Flask,jsonify


app=Flask(__name__)

@app.route('/<command>/<num1>/<num2>')
def Calculation(command,num1,num2):
    if type(num1)==str:
        num1=int(num1)
    if type(num2)==str:
        num2=int(num2)
    if command=='addition'or command=='add' or command=='sum':
        result={'addition':num1+num2}
    elif command=='subtraction' or command=='sub':
        result={'subtraction':num1-num2}
    elif command=='multiply':
        result={'multiply':num1*num2}
    elif command=='division':
        result={'division':num1/num2}
    else:
        result={'output':'Command not Found'}
    return jsonify(result)
    
    

if __name__=='__main__':
    app.run(port=5005) #it starts server on my system-server content


