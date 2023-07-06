class Vehicle:
    
    def start_engine(self):
        print("Engine started!!")
        
class Car(Vehicle):
    
    def drive(self):
        print("Driving the car") 
        
class Tesla(Car):
     
     def race(self):
         print("Tesla car")
         
my_car=Tesla()
my_car.start_engine()
my_car.drive()
my_car.race()
                      