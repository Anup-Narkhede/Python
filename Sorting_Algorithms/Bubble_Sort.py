#Bubble Sort

#complexity - O(n^2)
#unsorted array -- sorted array(formed rightmost)

a=[9,3,1,11]
n=len(a)


for i in range(n):                  # no of iterations
    swapped=False                   #set flag if array is already sorted complexity becomes O(n)
    for j in range(n-i-1):          # array index   -1 cannot compare last   -i for optimisation
        if(a[j]>a[j+1]):            #check if current index value > next index value
            a[j],a[j+1]=a[j+1],a[j] # swapping
            swapped=True
            #a=a+b  a=3 b=4  a=7      | a=a^b  xor logic if same then zero   | temp=a
            #b=a-b  b=3               | b=a^b                                | a=b  
            #a=a-b  now a=4 b=3       | a=a^b                                | b=temp
    if(swapped==False):
        break
    
print(a)    

"""
1)n-i-1  where i for optimisation and 1 for cannot compare last element
2)current>next
3)swap 
"""
