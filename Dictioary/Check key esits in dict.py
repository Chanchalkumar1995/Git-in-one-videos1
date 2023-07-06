dictionary={"a":1,"b":2,"3":3}

def check_present(a):
    return a in dictionary

print(check_present("a"))
print(check_present("z"))