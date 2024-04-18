def areavolume(l,b,h):
    area1=l*b
    vol1=l*b*h
    return area1,vol1

print("function with return value example")
a=int(input("enter the lenght:"))
b=int(input("enter the breadth:"))
print("area of rectangle")

c=int(input("enter the height"))

area,vol=areavolume(a,b,c)
print("area of the rectangle is:",area)
print("area of the rectangle is:",vol)
