x = 8

# 1- And Operatörü (ve)
# sonuc = 5 < x < 15
sonuc = (x > 5) and (x < 15)

# True ve true => True
# False ve true => False
# False ve False => False

hak = 1
devam = 'h'

sonuc = (hak > 0) and (devam == 'e')

# 2- or operatörü (veya)

sonuc = (x > 0) or (x % 2 == 0)

# True veya true => True
# False veya true => True
# False veya False => False

# 3- not operatörü
sonuc = not(x > 0)

# x, 5-10 arasında bir çift sayı mı ?

sonuc = ((x>5) and (x<10)) and (x % 2 == 0)
print(sonuc)
