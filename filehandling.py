# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:34:12 2019

@author: SONY
"""

#File Handling
filename='demand_table.txt'
"""f=open(filename,'r')
#mode: 'r': read file
#mode: 'w': write file
#mode: 'a': append vfile

header=f.readline()
#print(f.readline(),end='')
#print(f.readline(),end='')
#print(f.readline(),end='')
#f.close()
product_table=[]
for line in f:
    line1=line.split('\n')[0]
    #print(line1)
    product_details=line1.split(',')
    #print(product_details)
    #print(product_details)
    print(product_details,end='')
    product_table.append(product_details)
    
productc_demand=0
for product in product_table:
    productc_demand+=int(product[3])
print(productc_demand)"""

def SearchIndex(filename,query_string):
    f=open(filename,'r')
    header=f.readline()
    header1=header.split('\n')[0]
    header_list=header1.split(',')
    
    idx='none'
    col=0
    row=0
    
    for line_idx,line in enumerate(f):
        line1=line.split('\n')[0]
        product_details=line1.split(',')
        
        if query_string in product_details:
            row=1
            idx=line_idx+1
            
    if idx=='none':
        if query_string in header_list:
            idx=header_list.index(query_string)
            col=1
    return row,col,idx

row,col,idx=SearchIndex(filename,'Product D')
 




