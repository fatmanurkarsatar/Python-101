'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın.
   ** "random modülü" için "python random" şeklinde arama yapın
   **  100 üzerinden puanlama yapın. Her soru 20 puan.
   **  hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
       üzerinden hesaplansın.
'''

import random

sayi = random.randint(1,100) 
can = int(input('kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin =int(input('tahmin: '))
    
    if sayi == tahmin:
        print(f'tebrikler {sayac}.defada  bildiniz. Toplam puanınız: {100 - (100/can)*(sayac-1)}')
        break
    elif sayi >tahmin:
        print('yukarı')
    else:
        print('aşağı')    
        
    if hak == 0:
        print(f'hakkınız bitii. Tutulan sayı : {sayi}')    
        
        