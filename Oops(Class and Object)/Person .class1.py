class Person:
        name=None
        age=None
        email=None
        
        def __init__(self):
            print("I am called,Automatically") 

        def sleep(self):
            print("sleeping")
            
        def eating(self):
            print("eating")
        
       
               
pramod=Person() 
pramod.eating()
amit=Person()
amit.sleep()          