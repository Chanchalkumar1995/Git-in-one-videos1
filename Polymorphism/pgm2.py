#OverWritting/overriding is possible in polymorphism.
class Animal:
    
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    
    def sound(self):
        print("Dog sound")
        
animal=Animal()
animal.sound()

dog=Dog()
dog.sound()        