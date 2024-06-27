sayilar = [1,5,15,35,57,72,75,10]

 # 1- sayilar listesindeki her bir elemanı yazdırın.
# for sayi in sayilar:
#     print(sayi)
 
 # 2- sayilar listesindeki hangi sayılar 5'in katıdır?
# for sayi in sayilar:
#     if (sayi % 5 == 0):
#         print(sayi)
     
 # 3- sayilar listesinde sayıların toplamı kaçtır ?
# toplam = 0
# for sayi in sayilar:
#     toplam = toplam + sayi
# print(toplam) 
     
 # 4- sayilar listesindeki çift sayıların karesini alınız.
# for sayi in sayilar:
#     if (sayi %2 == 0):
#         print(sayi,sayi*sayi) 
        

urunler = ['iphone 8','iphone x','iphone XR','samsung S10']

# 5- urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.
# for urun in urunler:
#     print(urun[1])
    
#6- urunler listesinde içinde iphone geçen kaç ürün vardır?
count = 0
for urun in urunler:
    index = urun.find('iphone')
    if (index>-1):
        count += 1
print(count)        
   
    
     
 