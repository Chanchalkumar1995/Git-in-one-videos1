class Myclass:
    
     def __init__(self):
        self.public_val=10
        self._protected_val=11
        self.__private_val=12
        
        
     def public_method(self):
        print("This is public method")
        
        print(self._protected_val)
        self._protected_method()
        
     def _protected_method(self):
         print("This is protected method")
         
         print(self.__private_val)
         self.__private_method() 
         
     def __private_method(self):
         print("This is private method") 
         
                      
obj=Myclass()
print(obj.public_val)  
obj.public_method() 
