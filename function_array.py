# -*- coding: utf-8 -*-


def Array_Multiply(*args):
    t=[]
    count=0
    for i in args:
        count=count+1
        for idx in range(len(i)):
            if count==1:
                t.append(i[idx])
            else:
                t[idx]=t[idx]*i[idx]
    return t

out=Array_Multiply([2,5,7],[3,1,4],[6,4,4],[3,3,1])
print(out)


def Array_Sub(*args):
    t=[]
    count=0
    for i in args:
        count=count+1
        for idx in range(len(i)):
            if count==1:
                t.append(i[idx])
            else:
                t[idx]=t[idx]-i[idx]
    return t

out1=Array_Sub([2,5,7],[3,1,4],[6,4,4],[3,3,1])
print(out1)


def Array_Div(*args):
    t=[]
    count=0
    for i in args:
        count=count+1
        for idx in range(len(i)):
            if count==1:
                t.append(i[idx])
            else:
                t[idx]=t[idx]/i[idx]
    return t

out2=Array_Div([2,5,7],[3,1,4],[6,4,4],[3,3,1])
print(out2)

