class A:
    def method_a(self):
        print("Method A")
        
    def greet(self):
        print("HelloA")
            
        
class B:
    def method_b(self):
        print("Method B") 
        
    def greet(self):
        print("HelloB")          
        
class C(B,A): 
    def method_c(self):
        print("Method C")  
        
my_object=C()
my_object.greet() 
            