msg = "Python Kursumuza Hoş Geldiniz. Ben Fatma Nur Karsatar"

# sonuc = msg.upper()
# sonuc = msg.lower()
# sonuc = msg.title()
# sonuc = msg.capitalize()

# sonuc = "abc".islower() 

# sonuc = "   abc ".strip()
# sonuc = msg.split()
# sonuc = msg.split('.') 

# sonuc = "-".join(sonuc)

# index = msg.index('Hoş')
# sonuc = msg.startswith('P')  
# sonuc = msg.endswith('r')  

sonuc = msg.replace('Fatma','Selin')
sonuc = msg.lower().replace( ' ','-').replace('ş','s')

print(sonuc)