
def generateNext(d,num): 
    for i in range(1,11):
        print(num,end=",")
        num=num+d
       
    
        
C=float(input("Please input the starting for your series\n"))
s=float(input("Please input the d for your series\n"))
print ("The series produced by this method is:")
generateNext(s,C)