#create range
sq=[i**2 for i in range(10)]
print(sq)
#list Built in Function
num=list(range(2,20))
print(num)

#slicing
my_list=("Chanchal Kumar")
print(my_list[0:2]) #ch
print(my_list[2:]) #anchal kumar
print(my_list[:]) #chanchal kumar
print(my_list[::-1])#ramuk lahcnahc
print(my_list[:-1]) #chanchal kuma
my_list1=[1,2,3,4,5]
my_list1.extend([6,7,8])
print(my_list1)