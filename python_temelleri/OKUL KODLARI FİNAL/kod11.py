# i = 0
# while i<10:
#     işlemler
#     i+=1

baslangic = int(input("Başlangıç sayısını giriniz:"))
bitis = int(input("Bitiş sayısını giriniz: "))

tektoplam = cifttoplam = 0
teksayac = ciftsayac = 0

while baslangic<bitis:
    if baslangic%2==0:
        cifttoplam += baslangic
        ciftsayac += 1
    else:
        tektoplam += baslangic
        teksayac += 1
    baslangic += 1
    
ciftort = cifttoplam / ciftsayac
tekort = tektoplam / teksayac

print("Çift toplam =",cifttoplam)
print("Çift adet =",ciftsayac)   
print("Çift ortalama =",ciftort) 

print("Tek toplam =",tektoplam)
print("Tek adet =",teksayac)
print("Tek ortalama =",tekort)       
