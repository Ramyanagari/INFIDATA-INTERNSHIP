A={1,2,3,4,5}
B={4,5,6,7,8}
print("union of A and B is:",A.union(B))#| union symbol
print("union of A|B:",A|B)

print("intersection of A&B is:",A.intersection(B))
print("intersection of A&B is:",A&B)#& intersection symbol

print("A.difference(B) is:",A.difference(B))
print("B.difference(A) is:",B.difference(A))
print("A-B is",A-B)#- difference symbol

print("A^B is:",A^B)#^ symmetric_difference symbol
print("symmetric difference of Aand B",A.symmetric_differnce(B))