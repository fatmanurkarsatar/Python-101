from builtins import print
from itertools import product

sayi = [34,23,41,56,78,12,0,98,13]
print("Dizinin ilk elemanı =",sayi[0])
print(sayi[3])
print(sayi[8]) #eleman sayısı 9 max indis 8
print(len(sayi))
print(sayi)
print(sayi[len(sayi)-3])

print(sayi[0:5])
print(sayi[3:6]) # 3 ten 6 ya kadar yazar 6.yı yazmaz
print(sayi[:8]) #ilk 8 elemanı yazar
print(sayi[3:])
print(sayi[-1])
print(sayi[-2])

meyveler = ["elma","armut","nar","mandalina","çilek"]
print(meyveler[3])

meyveler += ["üzüm","muz","kiraz"]
print(meyveler)

meyveler.append("karpuz")
print(meyveler)

del meyveler[0]
print(meyveler)

meyveler.pop(0)
print(meyveler)

meyveler *=3
print(meyveler)

dizi = [0,2,1,6,8,8,9,0,3,2]
print(dizi)
dizi.sort()
print(dizi)
dizi.reverse()
print(dizi)
dizi.insert(0,5)
print(dizi)
dizi.insert(3,7)
print(dizi)

print(dizi.count(0))

dizi.clear()
print(dizi)

dizi = [2,4,5,7,8,9,0,1]
for i in dizi:
    print(i)
    
for i in range(len(dizi)):
    print(dizi[i])    
    
    
s = []

import random

for i in range(10):
    s.append(random.randint(0,100))
        
print(s)        