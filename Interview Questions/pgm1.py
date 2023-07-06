#how to check if a list empty in python.
my_list=[]
non_empty=[1,2,3,4,5]
is_empty=len(my_list)
if (is_empty == 0):
   print('list is empty')
else:
    print('List is non empty')
    
    #another way
    
list=[]
non_list=[1,2,3,4,5]   
 
def check_list(l):
    if len(l) == 0:
        print('list is empty')
    else:
        print('list is non empty')
check_list(list) 
check_list(non_list)       
          
