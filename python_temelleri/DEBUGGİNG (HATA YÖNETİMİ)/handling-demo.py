liste = ["1","2","5a","10b","abc","10","50"]

# 1: liste elemanları içindeki sayısal değerleri bulunuz.

# for x in liste:
#     try:
#         sonuc = int(x)
#         print(sonuc)
#     except ValueError:
#         continue    
    
# 2: kullanıcı 'q' değerini girmedikçe aldığınız 
# her inputun sayı olduğundan emin olunuz aksi halde 
# hata mesajı yazınız.

# while True:
#     sayi = input('sayı: ')
#     if (sayi == 'q'):
#         break
    
#     try:
#         sonuc = float(sayi)
#         print(f'girilen sayı: {sayi}')
#         break
#     except ValueError:
#         print('geçersiz sayı')
#         continue
    

# 3: dictionary ve key bilgilerini paranetre alarak 
# yapan get(d, key) fonkksiyonu hazırlayınız.

urun = {"urunadi":"samsung s10"}

# d = ["fiyat"] => KeyError

# get(d, "price") => None
# get(d,"urunadi") => samsung S10

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
    
print(get(urun, 'fiyat'))    
print(get(urun, 'urunAdi')) 