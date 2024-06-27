# 1- "Samsung S5,Samsung S6,Samsung S7,Samsung S8," elemanlarına ait bir liste oluşturunuz.
telefonlar = ["Samsung S5","Samsung S6","Samsung S7","Samsung S8",]
print(telefonlar)

# 2- liste kaç elemanlıdır ?
sonuc = len(telefonlar)

# 3- Listenin ilk ve son elemanı nedir ?
sonuc = telefonlar[0]
sonuc = telefonlar[-1]

# 4-"Samsung S5" değerini "Samsung S9" ile değiştirin.
# telefonlar[0] ="Samsung S9"
sonuc = telefonlar

# 5-"Samsung S6" Listenin bir elemanı mıdır ?
if "Samsung S6" in telefonlar:
      print("Samsung S6 liste içinde var.")

# 6- Listenin -3 indeksindeki değer nedir ?
sonuc = telefonlar[-3]

# 7- Listenin ilk 2 elemanını alın.
sonuc = telefonlar[0:2]

# 8- Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.
# telefonlar[-2:] = ["Samsung S9","Samsung S10"]
sonuc = telefonlar

# 9- Listenin üzerine "Iphone X" ve "Iphone XR" değerlerini ekleyiniz.
sonuc = telefonlar + ["Iphone X","Iphone XR"]

# 10- Listenin son elemanını silin.
del telefonlar[-1]
sonuc = telefonlar

# 11- Liste elemanlarını tersten yazdırınız.
sonuc = telefonlar[::-1]


# 12- Aşağıdaki verileri bir liste içinde saklayınız
      
      #kullaniciA: Yiğit Bilgi 2010, (70,60,70)
      #kullaniciB: Sena Turan  1999, (80,80,70)
      #kullaniciC: Ahmet Turan 1998, (80,70,90)
    
ogrenciA = ["Yiğit","Bilgi",2010,[70,60,70]]  
ogrenciB = ["Sena","Turan",1999,[80,80,70]]    
ogrenciC = ["Ahmet","Turan",1998,[80,70,90]]   
    
ogrenciler = [ogrenciA,ogrenciB,ogrenciC]   

for ogrenci in ogrenciler:
      ad = ogrenci [0]
      soyad = ogrenci[0]
      yas = {2021-ogrenci[2]}
      print(f"{ad} {soyad} {2021-ogrenci[2]} {ogrenci[3]}")
    
# 13- Liste elemanlarını ekrana yazdırınız.      

#for a in telefonlar:
      print(a)




print(sonuc)
