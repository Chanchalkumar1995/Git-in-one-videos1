#check if a key exits in a dictionary
dictionary={"a":1,"b":2,"3":3}

def check_present(a):
      if "a" in dictionary: 
          print("True")
      else:
          print("False")
          
print(check_present("a"))
print(check_present("z"))   

#another way with Defination and return also
dictionary={"a":1,"b":2,"3":3}

def check_present(a):
    return a in dictionary 

print(check_present("a"))
print(check_present("z")) 
    
    