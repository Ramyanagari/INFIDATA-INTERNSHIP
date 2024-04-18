t1=("A","B")
t2=(100,200)
print("t1 is:",t1)
print("t2 is:",t2)
l1=[]
l1=list(t1)
print("t1 is:",t1)
l2=[]
l2=list(t2)
print("t2 is:",t2)
l3=[]
l1=l2
l2=l3
print("l2 is:",l1)
print("l2 is:",l2)
t1=tuple(l1)
print("updated tuple is t1:",t1)
t2=tuple(l2)
print("updated tuple is t2:",t2)
