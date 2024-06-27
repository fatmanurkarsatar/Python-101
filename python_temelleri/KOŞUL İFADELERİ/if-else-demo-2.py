# Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.

benzinFiyat = 6.69
dizelFiyat = 5.86

ortalamaYakitTuketimi = float(input('100 km deki ortalama yakıt tüketimi: '))
gidilecekYol = float(input('gidilecek yol kaç km: '))
yakitTipi = input('yakıt tipiniz nedir: ')

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi 

print(toplamYakitUcreti)