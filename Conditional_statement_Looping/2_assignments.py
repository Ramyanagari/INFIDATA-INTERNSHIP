weight=float(input("enter the weight"))
numitems=int(input("enter the numitems"))

if weight<1:
    price=1.45
if weight>=1:
    price=1.15
total =weight*price
if numitems>=10:
    total=total*0.9
print("weight:",weight)
print("price:",price)
print("total:",total)