# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary şeklinde sakalyınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.
  
  
urunler = {
            '100': {'ad': 'Iphone 8', 'fiyat': '5000'},
            '101': {'ad': 'Iphone X', 'fiyat': '6000'},
            '102': {'ad': 'Iphone XR', 'fiyat': '7000'}
        }

# id = input('id: ')
# ad = input('ad: ')
# fiyat = input('fiyat: ')

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat,
# }


# id = input('id: ')
# ad = input('ad: ')
# fiyat = input('fiyat: ')

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat,
# }


# id = input('id: ')
# ad = input('ad: ')
# fiyat = input('fiyat: ')

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat,
# }

id = input('aramak istediğiniz ürün id')
urun = urunler[id]

print(f"id: {id} ürün adı: {urun['ad']} ürün fiyatı: {urun['fiyat']}")
# print(urunler)