a=1
b=0
try:
    print(x)
    print(a/b)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")
            
