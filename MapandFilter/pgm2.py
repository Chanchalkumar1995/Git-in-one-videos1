def square_me(a):
    return pow(2,a)
number=[1,2,3,4]
result=list(map(square_me,number))
print(result)

for i in result:
    print(i)