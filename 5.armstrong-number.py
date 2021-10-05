#Armstrong number. 153 => 1^3 + 5^3 +3^3 = 1+125+27= 153 [The sum of the cubes of digits of a number is equal to the original number.]

n=int(input("Enter no to check whether it is Armstrong no or not: "))
o=n                 #store n in new variale ...value of n will change due to further operations
sum=0
while(n>0):
    r= n % 10
    c= r**3
    sum = sum + c
    n= n //10
    
if(sum==o):
    print(o," is an Armstrong number")
else:
    print(o," is an Armstron number")

    
