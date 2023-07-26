
# insert 1billion rows
"""
Created on Sat Feb 29 14:47:59 2020

@author: SONY
"""
import time
import random


t1=time.perf_counter()
i=[192,185,154,129,180,165,117,105]
protocol=['TCP','HTTP','FTP','IP']
port=[80,90,95,100,200,205,1005]
filename='data1.csv'
rows=100_000
year=2020
with open(filename,'w')as f:
    str_='ID,Protocol,Port,Date,Time'
    f.write(str_)
    f.write('\n')
    for row in range(rows):
        time_=[str(random.randint(0,23)),str(random.randint(0,60)),
               str(random.randint(0,60))]
        date_=[str(random.randint(1,31)),str(random.randint(1,12)),
               str(year)]
        data=[str(random.choice(i)),str(random.choice(protocol)),
              str(random.choice(port))]
        time_data=':'.join(time_)
        date_data='/'.join(date_)
        final_data=','.join(data)
        data_entry=final_data+','+date_data+','+time_data
        f.write(data_entry)
        f.write('\n')
    
time.sleep(2)
t2=time.perf_counter()
elapsed_time=t2-t1
print(f'Execution Time:{elapsed_time} secs')


