#Write a program to find factorial of a given number


n=int(input("Enter no to find factorial: "))

fact = 1
for i in range(n,0,-1):
    if(i==1):
        print(i,end=" ")                #4*3*2*1=24
    else:
        fact = fact *i
        print(i,"*",end=" ")            #4*3*2*1*=24
print("=",fact)
