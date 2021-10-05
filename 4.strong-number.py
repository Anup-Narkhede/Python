# Writer a program to checke entered no is Strongnumber.
#eg.145=>1!+4!+5!=1+24+120=145[Strong no = The sum of the factorials of digits of a number is equal to the original number.]

n=int(input("Enter number to check whether it is strong number or not: "))
t=n         
sum=0
while(n > 0):
    r = n % 10                  #Seperates last digit          145 -> loop1) 5              loop2) 4               loop3) 1
    fact=1
    for i in range(1,r+1):  
            fact=fact*i         #find factorial of that last digit -> loop1) 5!             loop2) 4!              loop3) 1!
    
    print("factorial of ",r," is=",fact) 
    
    sum = sum + fact            #Addition of factorials               loop1) sum=5!         loop2) sum = 5! + 4!   loop3) sum = 5! + 4! + 1!
    n = n // 10                 #eliminate unit digit                 loop1) n becomes 14   loop2) n becomes 1     loop3) n becomes 0,program will go out of loop
    
print("\nAddition of factorials of digtis of",t,"is= ",sum)

if(sum == t):                                   
    print("\n",t," is a Strong number")
else:
    print("Hence,",t," is not a Strong number")
