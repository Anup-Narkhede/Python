#Write a program to check whether a natural number entered by user is an odd or even number


n=int(input("Enter a natural number to check whether it is Even or Odd:  "))

if (n % 2 == 0):                        # Modulus Operator:  gives remainder e.g. 12 % 4 =  0
    print(n," is an Even Number")
else:
    print(n," is an Odd Number")
    
    
