# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
# name = input('isminizi  giriniz: ')
# age = int(input('yaşınızı giriniz: '))
# education= input('eğitim bilginizi giriniz: ')
# if (age >= 18):
#     if (education == 'lise' or education == 'üniversite'):
#         print('ehliyet alabilir.')
#     else:
#         print(f'{name} ehliyet alamazsınız çünkü eğitim durumu yetersiz.')
# else:
#     print(f'{name} ehliyet alamazsınız çünkü yaşınız tutmuyor.')     
    

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık
# gelen not bilgisini yazdırınız.
#    0-24   => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5
# yazili1 = float(input('1.yazılı: '))
# yazili2 = float(input('2.yazılı: '))
# sozlu = float(input('sözlü: '))
# ort = (yazili1 + yazili2 + sozlu) / 3
# if (ort >= 0) and (ort < 25):
#     print(f'ortalamanız: {ort} ve notunuz: 0')
# elif (ort >= 25) and ( ort < 45):
#     print(f'ortalamanız: {ort} ve notunuz: 1')
# elif (ort >= 45) and ( ort < 55):
#     print(f'ortalamanız: {ort} ve notunuz: 2')
# elif (ort >= 55) and ( ort < 70):
#     print(f'ortalamanız: {ort} ve notunuz: 3')
# elif (ort >= 70) and ( ort < 85):
#     print(f'ortalamanız: {ort} ve notunuz: 4')
# elif (ort >= 85) and ( ort <= 100):
#     print(f'ortalamanız: {ort} ve notunuz: 5')
# else:
#     ('yanlış bilgi girdiniz.')    
 
       
# 3- Trafiğe çıkış tarihi alınan bir aracın zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım  => 1. yıl
#    2. Bakım  => 2. yıl
#    3. Bakım  => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesalayınız.
#    ** datetime modülünü kullanmanız gerekiyor.
#    (simdi) - (2018/8/1)  => gün

import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/7/11)')
tarih = tarih.split('/')

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

print(gun)

if (gun<=365):
    print('1.servis bakımı.')
elif (gun>365) and (gun<=365*2):
    print('2.servis bakımı.')
elif (gun>=365*2) and (gun<=365*3):
    print('3.servis bakımı.')
else:
    print('hatalı bilgi girdiniz.')        



print(simdi)
