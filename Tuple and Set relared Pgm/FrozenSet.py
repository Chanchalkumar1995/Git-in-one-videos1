#string=('h','g','u','i','r','y','p')
#fset1=frozenset(string)
#print("The Frozen is:")
#print(fset1)

set2={1,2,3,4,6}
set3={3,4,6,7,8}
my_set=set2.intersection(set3)
print(my_set)

set5={2,3,4,5,6,7}
set6={8,9,10,11,12}
my_set=set5.union(set6)
print(my_set)

set1={1,2,3,4,5,6}
set8={4,5,6,7,8,9}
my_set=set1.difference(set8)
print(my_set)

set1={1,2,3,4,5}
set2={2,3,4,}
subset=set2.issubset(set1)
print(subset)
supersubset=set2.issubset(set1)
print(supersubset)