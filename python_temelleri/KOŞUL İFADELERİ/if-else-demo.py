# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
# sayi1 = int(input("bir sayı giriniz: "))
# if 50<sayi1<100:
#     print('sayı 50 ile 100 arasındadır.')
# else:
#     print('sayı 50 ile 100 arasında değildir.')    

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
# sayi = int(input("bir sayı giriniz: "))
# if sayi>0 :
#     if (sayi % 2 == 1):
#         print('girilen sayı pozitif tek  sayıdır.')
#     else:
#         print('girilen sayı pozitif ancak tek değil.')    
# else:
#     print('girilen sayı negatif.')    

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız.
# _username = 'nurkar'
# _password = '1234'
# girilenUsername = input('username: ')
# girilenPassword = input('parola: ')
# if (girilenUsername.strip() == _username) and (girilenPassword.strip() == _password):
#     print('girilen username ve parola doğru.')
# else:
#     print('girilen bilgiler yanlış.')    

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# x = int(input("bir sayı giriniz: "))
# y = int(input("bir sayı giriniz: "))
# z = int(input("bir sayı giriniz: "))

# if x>y and x>z:
#     print("en büyük sayı x tir.")
# elif y>x and y>z:
#     print("en büyük sayı y dir.")
# else:
#     print("en büyük sayı z dir.")       

# 5-  Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamasını hesaplayınnız.
# vize1 = float(input("vize notunuzu giriniz: "))
# vize2 = float(input("vize notunuzu giriniz: "))
# final = float(input("final notunuzu giriniz: "))

# ort = (((vize1 + vize2) / 2) * 0.4 ) + (final * 0.6)

# #durum1
# if (ort>=50):
#     print("geçti")
# else:
#     print("kaldı")    

#durum2
# if (ort>=50):
#     if (final>=50):
#         print(f"öğrencinin not ortalaması: {ort} ve öğrenci geçti.")
#     else:
#         print(f"öğrencinin not ortalaması: {ort} ve öğrenci kaldı. Finalden en az 50 almalıdır.")
# else:            
#      (f"öğrencinin not ortalaması: {ort} ve öğrenci kaldı.")

#durum3
# if (ort>=50):
#      print(f"öğrencinin not ortalaması: {ort} ve öğrenci geçti.")
# else:
#     if (final>=70):
#         print(f"öğrencinin not ortalaması:")
             

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# 0-18.4     = Zayıf
# 18.5-24.9  => Normal
# 25.0-29.9  => 


# ad = input('adınız: ')
# kg = float(input('kilonuz: '))
# hg = float(input('boyunuz: '))


