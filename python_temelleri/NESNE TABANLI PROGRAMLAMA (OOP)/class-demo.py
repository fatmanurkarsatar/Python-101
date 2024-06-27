# Comment isminde bir sınıf oluşturunuz.
# Comment sınıfı username. text, likes,
# dislikes, isminde özelliklere sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla 
# yorumları ekrana yazdırınız.

class Comment:
    def __init__(self,username,text,likes,dislikes):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
        
c1 = Comment("sadikturan","güzel kurs",100,20)    
c2 = Comment("selaturan","gut kurs",10,200) 
c3 = Comment("süloturan","götü kurs",15,80) 
c4 = Comment("selamituran","güt kurs",90,0) 
c5 = Comment("sidikturan","popo kurs",6,56)   

comments = [c1,c2,c3,c4,c5]

for c in comments:
    print(f"{c.username}: {c.text}")
    print(f"likes: {c.likes} - dislikes: {c.dislikes}")
     
        