class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        if name == "John":
            print("Not a real name")
        else:
            self.__name=name  
            
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>=0:
            self.__age=age
        else:
            print("Invalid age value. Age cannot be negative")             
        
person=Person("pramod",25)
print(person.get_age())
person.set_age(-1)
 