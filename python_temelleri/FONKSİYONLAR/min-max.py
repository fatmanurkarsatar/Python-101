sayilar = [1,5,7,45,25,89]
harfler = ['a','h','c','d','z']
isimler = ['ahmet','fatmanur','emine','zişan','büşra']


# sonuc = min(sayilar)
# sonuc = max(sayilar)

# sonuc = min(harfler)
# sonuc = max(harfler)


sonuc = min(isimler) #ahmet olur çünkü alfabe a ile başlar
sonuc = max(isimler) #zişanay olur çünkü alfabe z ile biter

sonuc =min([len(isim) for isim in isimler]) 
sonuc =max([len(isim) for isim in isimler]) 

sonuc = max(isimler, key=lambda n: len(n))
sonuc = min(isimler, key=lambda n: len(n))

urunler = [
    {"title":"iphone x","price":5000},
    {"title":"iphone xr","price":6000},
    {"title":"iphone 11","price":7000}    
]

sonuc = min(urunler, key=lambda urun: urun['price'])['title']
sonuc = max(urunler, key=lambda urun: urun['price'])['title']

max = 0

for urun in urunler:
    if urun["price"]>max:
        max = urun["price"]
        

print(max)