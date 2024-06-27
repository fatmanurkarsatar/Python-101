website = "http://www.nurkarsatar.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?  
sonuc = len(kursAdi)
sonuc = len(website) 
# print(sonuc)

# 2- 'website' içinden www karakterlerini alınız.
sonuc = website[7:10]
# print(sonuc)

# 3- 'website' içinden com karakterini alınız.
karakterSayisi = len(website)
sonuc = website[karakterSayisi-3:karakterSayisi] 
# print(sonuc)

# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterleini alın.
sonuc = kursAdi[0:15]
sonuc = kursAdi[-15:]
# print(sonuc)

# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırınız.
sonuc = kursAdi[::-1]
# print(sonuc)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirimiz.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın. 
print('abc' * 3)

name, surname, age, job = 'Fatma','Seyit', 18, 'öğrenci'

# 9- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
name = 'Bora'
surname = 'Yılmaz'
age = 32
job = 'mühendis'

print(f"Benim adım {name} {surname} , yaşım {age} ve mesleğim {job}.")
