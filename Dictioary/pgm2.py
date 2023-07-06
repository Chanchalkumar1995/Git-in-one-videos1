my_dict={"t_student":[1,2,3,4],"t_student2":[5,6,7,8]}
print(my_dict)

my_dict={"l_student":(1,2,3,4),"l_student2":(5,6,7,8)}
print(my_dict)

#Dictionary within dictionary

my_dict={
    "S1":{"name":"chanchal","age":28 },
    "S2":{"name":"ajay","age":26},
    "S3":{"name":"deepak","age":24},
    }
print(my_dict)
print(my_dict["S2"]['age'])

#For iterate the values

for key in my_dict:# for loop is usedto navigate
    #print(key,my_dict[key])
    print(key)
    
    if "name" in my_dict:
        print("Name is a key in the dictionary")
        
    print(my_dict.get("name"))
    
    