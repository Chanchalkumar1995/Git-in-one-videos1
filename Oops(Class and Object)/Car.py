class Car:
    name=None
    color=None
    model_name=None
    
    def __init__(self,car_name,car_color,car_model_name):
        self.name=car_name
        self.color=car_color
        self.model_name=car_model_name
        
    def start_engine(self):
        print("starting the engine ->" + self.name) 
    
    def drive(self):
        print("Driving ->"+ self.name)  
    
    def print_all(self):
        print(self.name,self.color,self.model_name)

#How to give dat during run time
car_name=input("enter the car name \n")
car_color=input("enter the car color \n")
car_model_name=input("enter the car model name \n")

tesla=Car(car_name,car_color,car_model_name)

tesla.print_all()
tesla.start_engine()
tesla.drive()
tesla.name

