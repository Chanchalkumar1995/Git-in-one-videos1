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
        
person=Person("pramod",25)
print(person.get_name())
person.set_name("John")
print(person.get_name()) 
       