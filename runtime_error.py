#to handle the simple runtime error"
a=[1,2,3]
try:
    print("second elment=%d"%a[1])
    print("forth elemnt=%d"%a[3])
except IndexError:
    print("an error occured")
        
