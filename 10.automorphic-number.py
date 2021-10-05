#Automorphic number [It is a number whose square ends with the same digits as number itself, ex: 5 (25), 6 (36), 25(625)]

n=int(input("Enter a number to check whether it is automorphic number or not: "))

no_of_digits = (len(str(n)))    #object of type int has no len() hence it is typecasted to str
square = n**2
remainder = square % pow(10,no_of_digits)

print(" Square of ",n,"is = ",square," which ends with ", remainder,"\n\nHence, ")

if(n == remainder):
    print(n," is an Automorphic number")
else:
    print(n," is not an Automorphic number")
