
filename='Product_cat4.csv'
f=open(filename,'r')
next(f)
product=[]
for line in f:
    data=line.split('\n')[0]
    data1=data.split(',')
    discount=str(data1[5])
    if data1[2]=='Electronics':
        product.append(tuple(data1))
    elif data[2]=='Furniture':
        product.append(tuple(data1))
    elif data[2]=='Food':
        product.append(tuple(data1))
    elif data[2]=='Beverage':
        product.append(tuple(data1))
    elif data[2]=='Beauty':
        product.append(tuple(data1))
    elif data[2]=='Health':
        product.append(tuple(data1))
    elif data[2]=='Sports':
        product.append(tuple(data1))
    elif data[2]=='Fashion':
        product.append(tuple(data1))
    elif data[2]=='Fitness':
        product.append(tuple(data1))
    elif data[2]=='Kitchen':
        product.append(tuple(data1))
    elif data[2]=='Grocery':
        product.append(tuple(data1))
    elif data[2]=='Stationery':
        product.append(tuple(data1))
    elif data[2]=='Pet':
        product.append(tuple(data1))
    else:
        data[2]=='Other'
        product.append(tuple(data1))
print(product)
f.close()
