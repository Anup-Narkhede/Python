#Check whether given number is palindrome or not. [Check reverse and original no are same or not]. e.g 145


n=int(input("Enter number to check whether it is palindrome or not: "))
rev=0
c = n
while(n>0):
    
        r = n % 10                  # gives unit place digit.     145 -> loop1) 5              loop2) 4               loop3) 1
        rev = (rev*10) + r          # reverse no                         loop1) 5              loop2) 54              loop3) 541
        n = n // 10                  #eliminate unit digit               loop1) n becomes 14   loop2) n becomes 1     loop3) n becomes 0,program will go out of
    
    
if ( rev == c):
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")


