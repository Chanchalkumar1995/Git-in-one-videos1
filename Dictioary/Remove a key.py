dict={"a":1,"b":2,"c":3}

def remove_key(dict,key):
    if key in dict:
        del dict[key]
    return dict
print(remove_key(dict,"b")) 


