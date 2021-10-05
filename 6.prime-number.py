#Prime number. 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97


lowerlimit=int(input("Enter lower limit: "))
upperlimit=int(input("Enter Upper limit: "))

print("Prime numbers between ",lowerlimit,"to",upperlimit," :")

for i in range(lowerlimit,upperlimit + 1):
    counter=0
    for j in range(1, upperlimit):          
            if(i % j == 0):
                counter+=1
    if(counter == 2):                                #prime no is only divisible by 1 and itself i.e by 2 numbers only
        print(i, end=" ,")
