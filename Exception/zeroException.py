#Division by Zero Exception 
try:
    result=10/0
except ZeroDivisionError as error:
    print("Error:",error)  
    
    print("------------------")  
    
try:
     x=int(input("enter the number\n"))
     result=10/x
     print(result)
except ZeroDivisionError as error:
     print("Error:",error) 
except ValueError as error:
    print("Error:",error)
finally:
    print("I will be executed any how")
    
print("-------------------------------")

try:
    x=int(input("enter the number\n"))  
    result=10/x
    print(x)
except Exception as error:
    print("Exception:",error)
          
                    