t1=(10,12,2.4,"bengaluru",('a','b'))
l1=[]
l1=list(t1)#type conversion from tuple to that
print("list l1 is:",l1)
print("l1[3]:",l1[2])#positive indices
print("l1[-2]:",l1[-2])#negative indices
print("l1[4][0] is:",l1[4][0])
print("l1[4] is:",l1[4])
l1.reverse()
print("reverse of l1:",l1)#the list is updates here