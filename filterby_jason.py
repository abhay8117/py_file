#d={}
"""d=dict()
d['productID']=2900
d['product Name']='abc'"""
import random
import json
electronics=['AC','Refrigerator','TV','Computer','Mobile','Laptop','Keyboard',
             'Fan','LCD','Bulb','Earphone','Headphone','Memory Card','Tabelts',
             'DSLR','Camera','Powerbanks','SmartWatches','Printers','Cooler',
             'Monitors','Desktop PCs','Speakers','Soundbars','DTH SetUp box',
             'Pendrives','Charger','Washing Machine','Water Purifiers','Lens',
             'Geysers','Table Fans','Immersion Rod','Iron','Vaccum Cleaners',
             'Inverter','Sewing Machine','Air Purifiers','Stabilizer','Modem',
             'Mouse','Phone','Routers','Electric Wires','Electric Kettle',
             'Switch','Heater','Toaster','Joystick','Scanner','Xbox','Drone',
             'Remote','Harddrive','USB Cable','Spy Camera','Microwaves','RAM',
             'UPS','Powerbank','Adapter','Socket','Induction','Juicer','Mixer',
             'Blender','Tablet','Processor','Motherboard','HDMI','Microphone',
             'TV Tuner','Graphic Card','DVD RW']
elec_comp=['LG','Whirlpool','Hitachi','Samsung','Lloyd','Panasonic','Micromaxc',
           'Nokia','Bajaj','Usha','Crompton','Havells','Anchor','HP','HCL',
           'Sony','Dell','Acer','Asus']

product={'electronics':
                {23456:
                    {'Product Name':'Computer',
                     'Company':'HP',
                     'MRP':50000,
                     'Discount':10,
                     'Rating':4,
                     'Price':45000
                     },
                45877:
                    {'Product Name':'Computer',
                     'Company':'HP',
                     'MRP':48000,
                     'Discount':0,
                     'Rating':5,
                     'Price':48000
                     }
                }
            }
 
product1=product['electronics']
for k in range(300):
     data={random.randint(10000,100000):{
                 'Product Name':random.choice(electronics),
                 'Company':random.choice(elec_comp),
                 'MRP':random.randint(10000,50000),
                 'Discount':random.randint(20,30),
                 'Rating':5,
                 'Price':48000
                 }
            }
     product1.update(data)
     
#approach 1
#find all products DR>25
def Groupitems(products,category,DR):
        filtered_products={}
        product=products[category]
        for key,val in product.items():
            if val['Discount']>DR:
                filtered_products[key]=val
        return filtered_products

filtered_products=Groupitems(product,'electronics',10)
f=open('filtered_data.json','w')
json.dump(product,f,indent=2)
f.close()



"""filename='filtered_data.json'
f=open(filename,'r')
#json.dump(f)
data=json.load(f)
f.close()"""