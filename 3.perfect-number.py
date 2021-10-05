#Perfect number. 28 = 1 + 2 + 4 + 7 + 14 [Perfect number is a positive integer that is the sum of its proper positive divisors]

n=int(input("Enter no to check whether it is perfect no or not: "))
sum=0

for i in range(1, n):
    if(n % i == 0):
        sum = sum + i

if(n==sum):
    print(n," is a perfect number")
else:
    print(n,"is not a perfect number")
