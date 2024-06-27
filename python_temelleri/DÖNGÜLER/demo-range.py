#  1- Çarpım tablosu hazırlayınız

# for i in range(1,11):
#     print('*************')
#     for k in range(1,11):
#         print("{} x {} = {}".format(i,k,i*k))
        

# 2- girilen bir sayının asal olup olmadığınnı kontrol ediniz...
#    asal sayı 1 ve kendisi hariç tam böleni olmayan sayıya denir.
 
sayi = int(input("bir sayı giriniz: "))

asalmi = True

if (sayi == 1):
    asalmi = False 
    
for i in range(2,sayi):
    if(sayi % i == 0):
        asalmi = False
        break    
    
if asalmi: 
    print('sayı asaldır.')
else:
    print('sayı asal değildir.')       