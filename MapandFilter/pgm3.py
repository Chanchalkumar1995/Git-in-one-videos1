#find even from list
my_list=[1,2,3,4,5,6,7]

def even(x):
    return x % 2 == 0

even_num=filter(even,my_list)
print(even)
even_num=list(even_num)
print(even_num)
