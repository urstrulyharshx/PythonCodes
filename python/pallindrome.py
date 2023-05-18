def pallindrome(n,rev=0):
    if(n==0):
        return rev
    rev=rev*10 + (n%10)
    rev = pallindrome(n//10,rev)
    return rev
n=int(input("Enter any number: "))
x=pallindrome(n)
if(x==n):
    print("Entered number is pallindrome")
else:
    print("Entered number is not pallindrome")
    