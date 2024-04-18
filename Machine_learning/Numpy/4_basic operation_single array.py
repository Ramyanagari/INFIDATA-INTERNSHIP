import numpy as np

a1=np.array([11,2,3,4,5,6])
#add 1 to every element
print("Adding 1 to every element:",a1+1)

#subtract 2 from each element
print("Subtracting 2 from each element:",a1-2)

#multiply each element by 10
print("Multiplying each element by 10:",a1*10)

#square each element
print("Squaring each element:",a1**2)

#modify existing array
a1 *=2 #a1=a1*2
print("Doubled each element of original array:",a1)

#transpose of array
a2=np.array([[1,2,3],[3,4,5],[9,6,0]])

print("\nOriginal array:\n",a2)
print("Transpose of array:\n",a2.T)