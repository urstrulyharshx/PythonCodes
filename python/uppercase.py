def conVowUpp(str):
    N = len(str)
     
    str1 =""
     
    for i in range(N):
        if (str[i] == 'A' or str[i] == 'E' or
            str[i] == 'I' or str[i] == 'O' or
            str[i] == 'U'):
            c = (str[i]).lower()
            str1 += c
        else:
            str1 += str[i]
 
    print(str1)
str=input("Enter any string: ")
print(conVowUpp(str))