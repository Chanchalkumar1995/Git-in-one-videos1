#remove duplicates from list
my_list=[1,2,2,3,4,5,5,5]
non_dup=list(set(my_list))
print(non_dup)

#Another way
my_list1=[23,23,23,45,67,89,8,0]
non_dup=[]
for i in my_list1:
  if i not in non_dup:
        non_dup.append(i)
print(non_dup)