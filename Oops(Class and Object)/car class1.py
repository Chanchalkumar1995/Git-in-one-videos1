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
        print("Driving ->"+ self.name)  


tesla=Car("Tesla","Red", "model X")
lambo=Car("Lambo","blue","Urus") 


tesla.drive()
lambo.drive()



