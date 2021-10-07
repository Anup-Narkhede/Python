#Program to print sum of given numbers provided as command line argument [ command line arguments passed at time of execution]
#sys module  and  argv variable - type: list [first element of argv is file name]

#note: Run program from command line 
#ip: py filename.py  op: 0  no ip treated as 0
# ip:   py filename.py 10 20 30 40   op: 100

from sys import argv

a= argv[1:]         # slicing of first element in list argv
sum = 0
for x in a:
    sum = sum + int(x)  # typecasted to int as  input is treated as string
print("Sum is= ",sum)
