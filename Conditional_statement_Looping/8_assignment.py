i=int(input("enter i value"))
j=int(input("enter j value"))
k=int(input("enter k value"))

if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print(i,j,k)
