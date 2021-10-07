#Program to read 3 float values from keyboard with , seperation and print sum

a,b,c=[ float(x) for x in input("Enter 3 numbers seperated by , : ").split(",")]        
print("sum of three numbers is =",a+b+c)


#s=input("Enter 3 numbers")      #input from user as a string        '10 20 30'
#l=s.split("")                   #Splitting of string into list      ['10','20','30']     split() takes space as default seperator, we can pass anything as a seperator
#l1 = [float(x) for x in l]      # new l1 list is created with typecasted datatype as a float   [10.0  20.0  30.0]
#a,b,c = l1                      #list unpacking                    a=10.0  b=20.0  c=30.0
#print("sum",a+b+c)
