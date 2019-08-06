num=56
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime")
            break
else:
 print(num,"is a prime")
