#Involves multiple class which is driving from single class only.
class Animal:
   
    def speak(self):
        print('Animal speak')
        
class Dog (Animal):
    
    def bark(self):
        print("woof!!")
        
class Cat(Animal):
    
    def meow(self):
        print("Meow!!")                
        
my_dog=Dog()
my_dog.speak()
my_dog.bark()  

my_cat=Cat()
my_cat.speak()
my_cat.meow()     