A=frozenset([2,3,4,5,6])
B=frozenset([4,5,6,7,8])
print("set A is",A)
print("set B is",B)


#frozenset is fixed so we cant,t able to add a new elements
#A.add(10)
print("set A is:",A)

print("A.union(B) is:",A.union(B))