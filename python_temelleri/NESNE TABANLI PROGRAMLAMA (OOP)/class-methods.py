class User:
    
    active_users = 0
    
    @classmethod
    def display_active_users(cls): 
        return f"{cls.active_users} tane aktif kullanıcı var."
    
    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(',')
        return User(first,last,age)
    
    def __init__(self,first,last,age):
        print(self)
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
         
    def full_name(self):
        return f"{self.first} {self.last}"   
    
    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan çıkış yaptı."
    
    
# print(User.display_active_users)    
# userA = User("melih","cevdet",78)    
# userB = User("selim","ceviz",98)  
# userC = User("selina","selim",98)  

ali = User.from_string("ali,korkmaz,20")
print(ali.first)



