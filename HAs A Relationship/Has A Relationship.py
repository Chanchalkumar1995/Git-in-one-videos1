#It will help us to do more abstraction.
# It is not Inheritance.
class Engine:
    
    def boot_engine(self):
        print("Booted")
        
class Vehicle:
    
     def start_engine(self):
         Engine().boot_engine()
         print("start engine")
         
v=Vehicle()
v.start_engine()               