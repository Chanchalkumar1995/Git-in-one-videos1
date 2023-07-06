my_marks=[]
print(type(my_marks))

my_marks.insert(0,91)
my_marks.insert(1,97)
my_marks.insert(1,77)
print(my_marks)

my_marks.append(89)
print(my_marks)

print(len(my_marks))
my_marks.remove(91)
print(my_marks)

#nestedlist

nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])

nested_list[0]=["abc","ef",'ck']
print(nested_list[0])

dup_list=[1,1,1,1,1,1,1,1,1]
print(dup_list)

mix_list=["Apple",123,True]
print(mix_list)