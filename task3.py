fin = open('products.csv','r',encoding='utf-8-sig')
title = fin.readline().strip()
products = [x.strip().split(';') for x in fin]
fin.close()
#products[0] - category
#products[1] - product
#products[2] - date
#products[3] - price per unit
#products[4] - count
dminn = {}
minn = 100000
for x in products:
    if x[0] in dminn:
        if float(x[4])<minn :
                minn = float(x[4])
                dminn[x[0]]= minn
    else:
        dminn[x[0]]=float(x[4])
print(dminn)                
while True:
    st = input('Введите название категории:')
    if st=='молоко':
        break
    for x in products:
        if x[0]==st and float(x[4])==dminn[x[0]]:
            print(f'В категории: {x[0]} товар: {x[1]} был куплен {x[4]} раз')
            break
    else:
        print('Такой категории не существует в нашей БД')
    
