# Write a pgm with 2 input and power also use it.
user1=int(input("enter the number and i will do num^2\n"))

def powby2(num):
    return pow(2,num)
result=powby2(user1)
print(result)

# use lambda to write this pgm
result=lambda num:pow(2,num)
print(result(3))