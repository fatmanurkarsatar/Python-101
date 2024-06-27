def hosgeldin():       #fonksiyon parametre almıyor
    print("Hoşgeldin: :)")
    
hosgeldin()    
hosgeldin() 
hosgeldin() 

def merhaba(isim):  #fonksiyon parametre alıyor
    print("merhaba",isim) 
    
isim = input("isminizi giriniz:")
merhaba(isim) 

def carp(a,b):
    return a*b

print(carp(2,3))   