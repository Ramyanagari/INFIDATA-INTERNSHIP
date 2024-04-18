def even(list):
    new = []
    for i in list:
        if i%2 == 0:
            new.append(i)
    return new
li=[]
n=int(input("Enter size of list"))
for i in range(0,n):
    e= int(input("Enter element of list"))
    li.append(e)


print("Even numbers in ", li)
print(even(li))
