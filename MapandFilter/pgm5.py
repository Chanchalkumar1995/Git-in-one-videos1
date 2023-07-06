#Compare with each elements
my_list=[1,2,45,67,89,99,101,150]
def find_large_element(numbers):
    large_element=numbers[0]
    for number in numbers:
        if number > large_element:
            large_element=number
    return large_element
result=find_large_element(my_list)
print(result)