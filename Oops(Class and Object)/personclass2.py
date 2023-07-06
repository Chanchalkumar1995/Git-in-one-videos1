class Person:
        name=None
        age=None
        email=None
        
        def __init__(self):#default constractor
             print("I am called,Automatically") 
        
        def __init__(self,name,age,email):#parameter constractor
            self.name=name
            self.age=age
            self.email=email
            
        def sleep(self):
            print(self.name + " is sleeping ")
            
        def eating(self):
            print(self.name + " is eating ")
        
       
               
pramod=Person("Chanchal","28","7471@gmail.com") #object1
pramod.eating()
amit=Person("Amit","32","8951@gmail.com")#object2
amit.sleep()          