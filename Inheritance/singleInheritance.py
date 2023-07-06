class Animal:
    
    def _speak(self):
        print("Animal speaking")
        
class Dog(Animal):#Child class has access to all methods and variables. 
    
    def bark(self):
        print("woof")
  
mydog=Dog()  
mydog._speak() 
mydog.bark()             