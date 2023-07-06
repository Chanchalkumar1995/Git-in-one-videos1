#class and object-car
#data member - name,color,model_name
#Method - Start_Engine,Drive
#Tesla,Lambo

class Car:
    name=None
    color=None
    model_name=None
    
    def __init__(self,name,color,model_name):
        self.name=name
        self.color=color
        self.model_name=model_name
        
    def start_engine(self):
        print("starting the engine ->" + self.name) 
        
    def drive(self):
        print("Driving ->" + self.name)  

    def print_all(self):
     print(self.name,self.color,self.model_name)

tesla=Car("Tesla","Red", "model X")
lambo=Car("Lambo","blue","Urus")  

tesla.print_all()
print(tesla.name)
tesla.drive()
lambo.print_all()
print(lambo.name)
lambo.drive()


