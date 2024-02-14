fin = open('products.csv','r',encoding='utf-8-sig')
title = fin.readline()
products = [x.strip().split(';') for x in fin]
fin.close()
for i in range(1,len(products)):
    for j in range(i,0,-1):
        if products[j][0]<products[j-1][0]:
            products[j],products[j-1]=products[j-1],products[j]
#products[0] - category
#products[1] - product
#products[2] - date
#products[3] - price per unit
#products[4] - count
maxx = 0
prod = ''
for x in products:
    print(x)
    if x[0]=='Выпечка' and float(x[3])>maxx:
        maxx = float(x[3])
        prod = x[1]
print(f'В категории: Выпечка самый дорогой товар: {prod} его цена за единицу товара составляет {maxx}')
