def fact(n):
    if(n==0):
        print("Enter a number greater than 0:")
    elif(n==1):
        return 1
    else:
        return fact(n*(n-1))
n=int(input("Enter the number: "))
x=fact(n)
print(x)
    
    