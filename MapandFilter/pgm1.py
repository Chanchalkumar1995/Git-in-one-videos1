my_list=[1,2,3,4,5,6]

def Double_Me(a):
    return a*2

#result=map(Double_Me,my_list)
#print(result)

#for i in result:
 #   print(i)
    # another way to prunt map instead using for loop
result=list(map(Double_Me,my_list)) 
print(result)  
    