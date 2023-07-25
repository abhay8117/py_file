# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:48:44 2019

@author: SONY
"""

import random

electronics=['AC','Refrigrator','TV','Computer','Mobile']
DR_ele=[10,12,15,20,25]
furniture=['Sofa','Chair']
DR_fur=[10,15]
food=['Burger','Samosa','Biscuit']
DR_fd=None
beverage=['Tea','Coffee','Juice','Soft Drink']
DR_bvrge=[None,None,None,2]
product=['AC','Refrigrator','TV','Computer','Mobile','Burger','Samosa',
         'Biscuit','Sofa','Chair','Tea','Coffee','Soft Drink','Shoe']
MRP=[45000,25000,10999,12999,21000,40,10,10,1000,11000,10,10,20,700]

total_products=len(product)
header=['Product ID','Product','Category','MRP','Discount','Price']
header_pattern='%s,%s,%s,%s,%s,%s'


filename='Product_cat1.csv'
f=open(filename,'w')
f.write(header_pattern%tuple(header))
f.write('\n')


def FindDiscount(DR_category,item_list,item):
    discount_rate=None
    if isinstance(DR_category,list):
        idx=item_list.index(item)
        discount_rate=DR_category[idx]
    return discount_rate

def FindCategory(item):
    if item in electronics:
        category='Electronics'
        DR_category=DR_ele
        item_list=electronics
    elif item in furniture:
        category='Furniture'
        DR_category=DR_fur
        item_list=furniture
    elif item in food:
        category='Food'
        DR_category=DR_fd
        item_list=food
    elif item in beverage:
        category='Beverage'
        DR_category=DR_bvrge
        item_list=beverage
    else:
        category='Other'
        DR_category=None
        item_list=None
    discount_rate=FindDiscount(DR_category,item_list,item)
    return category,discount_rate
           
pattern='%d,%s,%s,%d,%d,%.2f'

for idx,product in enumerate(product):
    PID=random.randint(0,10000)
    PName=product
    PMRP=MRP[idx]
    CAT,PDR=FindCategory(product)
    if PDR==None:
        PDR=0
    PR=(1-PDR/100)*PMRP
    entry=pattern %(PID,PName,CAT,PMRP,PDR,PR)
    f.write(entry)
    f.write('\n')
f.close()
