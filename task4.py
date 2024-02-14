fin = open('products.csv','r',encoding='utf-8-sig')
title = fin.readline().strip()
products = [x.strip().split(';') for x in fin]
fin.close()
#products[0] - category
#products[1] - product
#products[2] - date
#products[3] - price per unit
#products[4] - count
for x in products:
    promo = x[1][0].upper()+x[1][1].upper()+x[2][0]+x[2][1]+x[1][-1].upper()+x[1][-2].upper()+x[2][4]+x[2][3]
    x.append(promo)
fout = open('product_promo.csv','w',encoding='utf-8-sig')
fout.write(title+';promocode\n')
for x in products:
    s = ';'.join(x)+'\n'
    fout.write(s)
fout.close()
