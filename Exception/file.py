try:
    file=open('C:\python\Exception\chanchal6.txt','r')
    print(file.read())
    file.close()
except FileNotFoundError as e:
    print("File Not Found!!!",e)    
    
    
    #Another way
try:
    file=open('C:\python\Exception\chanchal6.txt','r')
    contents=file.read()
    print(contents)
    
except FileNotFoundError:
    print("File Not Found!!!") 
except IOError:
    print("An error occured while reading the file")
else:
    print("File reading completed successfully")    
       