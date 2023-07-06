class A:
    
    def greet(self):
        print("Hello from class A")
        
class B:
    
    def greet(self):
        print("Hello from class B")
        
class C(A,B):
    pass  

class D(B,A):
    pass

obj1=C()
obj1.greet()   

obj1=D()
obj1.greet()  

print(C.mro()) 
print(D.mro())