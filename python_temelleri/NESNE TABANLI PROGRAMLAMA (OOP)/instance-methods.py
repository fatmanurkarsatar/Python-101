class Person:
    
    # yapıcı metodlar (constructor)
    def __init__(self,name,surname,year):
        
        # object attrıbutes , instance attributes
        self.name = name
        self.surname = surname 
        self.year = year
    
    # Instance methods
    def intro(self):
        return f"benim adım {self.name} ve soyadım {self.surname}"
    
    def calculate_age(self):
        return f"{2022-self.year}"
        
    
# object, Instance        
p1 = Person("Suna","Turro",1993)  
p2 = Person("sevil","Sevimli",1997)

print(p1.intro())   
print(p2.intro())

print(p1.calculate_age())
print(p2.calculate_age())
 