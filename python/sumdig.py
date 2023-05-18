def sumdigit(str):
    sum=0
    for digit in str:
        sum=sum + int(digit)
    return sum
    
str=input("Enter any string of numbers: ")
print(sumdigit(str))