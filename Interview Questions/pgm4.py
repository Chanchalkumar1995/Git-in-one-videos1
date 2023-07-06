#check for sublist in list
list=[1,2,3,4,5,6,7,8]
sublist=[]
match list:
 case x if sublist in x:
     print('present')
 case x if sublist not in x: 
     print("not present")
    