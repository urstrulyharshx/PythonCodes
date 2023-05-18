def fibo(n):
    if(n==0):
        return 0;
    elif(n==1):
        return 1;
    else:
        return fibo(n-2) + fibo(n-1);
n=int(input("Enter the term upto which you want to print series: "))
print("Fibonacci series: ")
for n in range(0,n):
    print(fibo(n),end=" ")
    
    