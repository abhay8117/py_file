# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:17:21 2019

@author: SONY
"""

import random
import time
first_name=['Abhay','Santosh','Sanjeev','Koustabh','Vikas','Anas','Shewta','Sanjay','Harsh','Suhani',
            'Shardha']
last_name=['Kumar','Goyal','Solanki','Singh','Chauhan']
salary=[1000,5000,10000,20000,15000,12000,18000]
department=['Sales','Engineering','Developer','Admin','Support','Finance']
company=['TCS','Ibibo','Wipro','Capegimni','Google','Intel','Accenture',
         'Cognizant']
total_entry=1_000_000
filename='employee_detail2.txt'
f=open(filename,'w')
t1=time.perf_counter()
for entry in range(total_entry):
    firstname=random.choice(first_name)
    lastname=random.choice(last_name)
    salary_=random.choice(salary)
    dep=random.choice(department)
    comp=random.choice(company)
    ID=firstname[:2]+lastname[:2]+dep[:2]+str(random.randint(0,10000))+comp[:2]
    data=ID+','+firstname+','+lastname+','+dep+','+str(salary_)+','+comp
    f.write(data)
    f.write('\n')
f.close()
t2=time.perf_counter()
print('total time execution=',t2-t1,'secs')

#Read the file you have created and find all persons in sales department and 
#create a new .txt file named filtered_data.txt and insert all results
    
