# Reverse number=> Input: 5678, output =>8765

n=int(input("Enter a natural number: "))
print("Reverse of ",n, end= " = ")
reverse = 0
while(n > 0):
    r = n % 10
    reverse = (reverse*10) + r
    n = n //10
print(reverse)
