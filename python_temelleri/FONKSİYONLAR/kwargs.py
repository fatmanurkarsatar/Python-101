def disPlayUser(*args):
    print(type(args))
    print(args)
    
disPlayUser()

def disPlayUser(**kwargs): 
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")  
    
disPlayUser(username="nurka")
disPlayUser(username="nurka", email="nurka@gmail.com", country="türkiye") 

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value 1", key2 = "value 2")    