t1=(2,3,5,6,8,20)
print("t1 id:",t1)
l1=[]
l1=list(t1) #type conversion
print("list l1 id:",l1)
num=int(input("enter the element to add"))
l1.append(num)
t1=tuple(l1)#type conversion
print("update tuble id:",t1)