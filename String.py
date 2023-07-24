# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:24:24 2019

@author: SONY
"""

header='First_Name,Last_Name,Age,Company,Location'
entry1='Sanjeev_Kumar,27,Tcs_Noida'
entry2='Rahul_Yadav,25,Wipro_Noida'
entry3='Santosh_Kumar,28,HCL_Gurgaon'
entry4='Asif_Iqbal,28,Aptron_Noida'
entry5='Abhay_Kumar,25,Aptron_Gurgaon'

# Method 1
h1=header.split(',')
FN=h1[0]
LN=h1[1]
Age_field=h1[2]
Comp_field=h1[3]
Loc_field=h1[4]
FN1=FN.split('_')
FN_field=FN1[0]+' '+FN1[1]
LN1=LN.split('_')
LN_field=LN1[0]+' '+LN1[1]

e1=entry1.split(',')
N_e1=e1[0].split('_')
FN_e1=N_e1[0]
LN_e1=N_e1[1]
Age_e1=e1[1]
CN_e1=e1[2].split('_')
Comp_e1=CN_e1[0]
Loc_e1=CN_e1[1]

data=[FN_field,FN_e1,LN_field,LN_e1,
      Age_field,Age_e1,Comp_field,Comp_e1,
      Loc_field,Loc_e1]

# Method 2

header_list=[]
h=header.split(',')
for field in h:
    if '_' in field:
        a=field.split('_')
        a1=a[0]+' '+a[1]
        header_list.append(a1)
    else:
        header_list.append(field)


entry1_list=[]
e1=entry1.split(',')
b=e1[0].split('_')
b1=e1[2].split('_')
entry1_list.append(b[0])
entry1_list.append(b[1])
entry1_list.append(e1[1])
entry1_list.append(b1[0])
entry1_list.append(b1[1])

data1=[]
data1.append(header_list[0])
data1.append(entry1_list[0])
data1.append(header_list[1])
data1.append(entry1_list[1])
data1.append(header_list[2])
data1.append(entry1_list[2])
data1.append(header_list[3])
data1.append(entry1_list[3])
data1.append(header_list[4])
data1.append(entry1_list[4])


        
# Method 3

def ProcessHeader(string):
    header_titles=[]
    ht=header.split(',')
    for field1 in ht:
        if '_' in field1:
            x=field1.split('_')
            x1=x[0]+' '+x[1]
            header_titles.append(x1)
        else:
            header_titles.append(field1)
    return header_titles

header_l=ProcessHeader(header)

def ProcessEntry(entry):
    entry_titles=[]
    et=entry.split(',')
    for value in et:
        if '_' in value:
            y=value.split('_')
            y1=y[0]
            y2=y[1]        
            entry_titles.append(y1)
            entry_titles.append(y2)
        else:
            entry_titles.append(value)
    return entry_titles
        
entry_l=ProcessEntry(entry2)

data2=[header_l[0],entry_l[0],header_l[1],entry_l[1],header_l[2],entry_l[2],
       header_l[3],entry_l[3],header_l[4],entry_l[4]]
print(data2)

    