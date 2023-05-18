str1=input("Enter any string: ")
str2=input("Enter any string: ")
str1=str1.lower()
str2=str2.lower()
if(len(str1)== len(str2)):
    sstr1=sorted(str1)
    sstr2=sorted(str2)
    if(sstr1==sstr2):
        print("Anagrams")
    else:
        print("are not anagrams")
    
