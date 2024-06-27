"""
urunA = 5500
urunB = 6000
urunC = 7000

kdv = 0.2

print(urunA + (urunA * kdv))
print(urunB + (urunB * kdv))
print(urunC + (urunC * kdv))
"""

from typing import NoReturn


sayi1 = 10
sayi2 = 20

# 3sayi => yanlış bir kullanım.değişkenler sayı ile başlayamaz.

sayi3 = 30
# sayi@ = 40 # yanlış

# sayi 4 = yanlış.değişkenler arasında boşluk olmayacak

sayı5 = 50 #türkçe karakter içermemelidir.

yas = 20 # büyük küçük harf duyarlılığı vardır.
YAS = 30

print(yas)
print(YAS)

a ,b ,c = 10, 20, 30
print(a,b,c)

x = 1
print(type(x))

y = 1.5
print(type(y))

name = 'fatmaNur'
print(type(name))

isStudent = True
isStudent = False

print(type(isStudent))

x, y, name, isStudent = 1, 1.5, "fatmaNur", False

a = 10
b = 20

toplam = a + b
print(toplam)