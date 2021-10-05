#Sum of digits. [e.g. for 1234, 1 + 2 + 3 + 4 = 10]

n=int(input("Enter no: "))
temp=n              #value of n will change in further mathematical operations
sum = 0
while(n > 0):
    r = n % 10
    sum = sum + r
    n = n //10
print("Sum of digits of",temp," =",sum)
