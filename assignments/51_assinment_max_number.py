def maximum(a,b,c):
    if(a >=b) and (a >= c):
        largest = a


    elif(b >=a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest

a=int(input("enter the first in number is:"))
b=int(input("enter the first in number is:"))
c=int(input("enter the first in number is:"))
print("the largest number is:",maximum(a,b,c))