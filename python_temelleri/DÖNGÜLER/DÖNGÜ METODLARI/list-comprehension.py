liste = [10,4,7,9,70]

sayilar = []


for i in liste:
    i *= 2
    sayilar.append(i)

# sayilar = [i*2 for i in liste]

isim = "Ahmet"
isimler = ["ahmet","ali","çınar","deniz"]


sonuc = [c.upper() for c in isim]
sonuc = [str(sayi) for sayi in liste]
sonuc = [i.lower() for i in isimler]

print(sonuc)    