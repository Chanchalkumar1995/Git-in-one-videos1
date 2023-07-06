#Defination Function
def num2(num):
    if num>50:
        print("greater than 50")
    else:
        print("less than 50")
        
num=num2(34)

#lambda function
r=lambda num: "Greater than 50" if num>50  else "Lower than 50"
print(r(45))   

r2= lambda x:x**2 if x>0 else (x*2 if x<0 else 0) 
print(r2(3))    
print(r2(-2))
print(r2(0))