import linecache

l1=[4,5,6,7,8,10,15,5]
print("l1 id:",l1)
print("lenght of l1:",len(l1))
print("max element in l1:",max(l1))
print("min element in l1:",min(l1))
print("sum of the l1 is:",sum(l1))
print("element count of 5 is:",l1.count(5))
l1.reverse()
print("reverse of l1:",l1)
print("element index:",l1.index(10))
l1.clear()
print("using clear():",l1)