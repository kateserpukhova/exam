fin = open('products.csv','r',encoding='utf-8-sig')
title = fin.readline().strip()
products = [x.strip().split(';') for x in fin]
fin.close()
#products[0] - category
#products[1] - product
#products[2] - date
#products[3] - price per unit
#products[4] - count
summ=0
for x in products:
    total = float(x[3])*float(x[4])
    x.append(str(total))
    if x[0]=='Закуски':
        summ+=total
print(summ)
fout = open('products_new.csv','w',encoding='utf-8-sig')
fout.write(title+';total\n')
for x in products:
    s = ';'.join(x)+'\n'
    fout.write(s)
fout.close()

    
    
    
