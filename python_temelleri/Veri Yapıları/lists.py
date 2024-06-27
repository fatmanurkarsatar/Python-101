msg = "Python Kursumuza Hoş Geldiniz. Ben Nur Kar".split()

sayilar = [1,3,5,7,9]

sonuc = sayilar
sonuc = sayilar[0]
#sonuc = sayilar[5] #IndexError: list index out of range

print(sonuc)

isimler = ['ela','can','ada','nur']

sonuc = isimler[3]
# print(type(sayilar[0]))

listeAli = ['ali',20]
listeAhmet = ['ahmet',22]

sonuc = listeAli[0]
sonuc = listeAhmet[1] 

#ogrenciler = [["ali",20],["ahmet",22]]
ogrenciler = [listeAli,listeAhmet]

sonuc = ogrenciler[0][0]
#sonuc = ogrenciler[1][0]

print(sonuc)