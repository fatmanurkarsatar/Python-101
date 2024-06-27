# kullanıcıyı 0 ile 100 arasında sayı girmeye zorlayacağız.

v = int(input("lütfen 0 ile 100 arasında bir sayı giriniz:"))

while True:
    if v>=0 and v<=100:
        break
    else:
        print("Lütfen 0- 100 aralığında giriniz!")
        v = int(input("lütfen 0 - 100 arasında bir sayı giriniz:"))
        
f = int(input("lütfen 0 ile 100 aralığında bir sayı giriniz:")) 

while True:
    if f>=0 and f<=100:
        break
    else:
        print("lütfen 0-100 aralığında bir sayı giriniz:") 
        f = int(input("lütfen 0-100 arasında bir sayı giriniz:")) 
    
ort = v*0.4 + f*0.6 
print("ortalama =",ort)          