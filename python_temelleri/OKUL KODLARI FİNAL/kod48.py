# Girilen 2 Sayıyı Toplayan Python Örneği
# sayi1 = int(input("bir sayı giriniz:"))
# sayi2 = int(input("bir sayı giriniz:"))
# sonuc = (sayi1 + sayi2)
# print(sonuc)


# Girilen 2 Sayının Ortalamasını Bulan Python Örneği
# sayi1 = int(input("bir sayı giriniz:"))
# sayi2 = int(input("bir sayı giriniz:"))
# sonuc = (sayi1 + sayi2) / 2
# print(sonuc)


# Girilen Vize ve Final Notu Ortalaması Hesaplayan Python
# v = int(input("vize notunuzu giriniz:"))
# f = int(input("final notunuzu giriniz:"))
# sonuc = v*0.4 + f*0.6
# print(sonuc)


# Girilen 3 Yazılı Notunun Ortalamasını Bulan
# x = int(input("yazılı notunuzu giriniz!"))
# y = int(input("yazılı notunuzu giriniz!"))
# z = int(input("yazılı notunuzu giriniz!"))

# ort= (x+y+z)/3

# if ort>=50:
#     print("geçti")
# else:
#     print("kaldı") 
       
# print(ort)


# Girilen Sayının Tek mi Çift mi Olduğunu Bulan Python
# sayi = int(input("bir sayı giriniz:"))

# if sayi%2==0:
#     print("sayı çifttir.")
# else:
#     print("sayı tektir.")    


# Girilen Sayının Pozitif, Negatif, ya da 0 Olduğunu Bulan Python
# sayi = int(input("bir sayı giriniz:"))

# if sayi>0:
#     print("sayı pozitiftir.")
# elif sayi == 0:
#     print("sayı sıfıra eşittir")
# else:
#     print("sayı negatiftir.") 


#Yaşı Girilen Kişinin Ehliyet Alıp Alamayacağını Gösteren Python       
# yas = int(input("yaşınızı giriniz:"))

# if yas>=18:
#     print("ehliyet alabilir")
# else:
#     print("ehliyet alamaz")    


# 1-100 Arası Sayıları Ekranda Listeleyen Python
# for i in range(1,101):
#     print(i)


# 1-100 arası Çift Sayıları Listeleyen Python
# for i in range(1,101):
#     if i%2==0:
#         print(i)


#  1-100 Arası Tek Sayıları Listeleyen
# for i in range(1,101):
#     if i%2!=0:
#         print(i)


#  1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan Python
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         print(i)


#  1 den Kullanıcının Girdiği Sayıya Kadar Sayıları Listeleyen Python
# sayi = int(input("sayı giriniz:"))
# for i in range(1,int(sayi+1)):
#     print(i)


# Kenarları Girilen Dikdörtgenin Alanı ve Çevresini Bulan Python 
# uk = int(input("uzun kenarı giriniz:"))
# kK = int(input("kısa kenarı giriniz:"))

# alan = uk*kK
# cevre = (uk+kK) * 2
# print(alan,cevre)

 
# Python Fonksiyon Kullanarak Dikdörtgen Alanı 
def dikdortgenAlan(genislik, yukseklik):
    alan = float(genislik) * float(yukseklik)
    print("Alan :",alan)
    return alan

gen = input("genişlik :")

yuk = input("yükseklik :")

dikdortgenAlan(gen, yuk)


