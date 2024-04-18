#IMPORTING NECCESSARY LIBRARIES
import numpy as np #used for matrix calculations

#MATRIX A
a=np.array([[1,2,3],   #array creation
           [4,5,6]])

print("array elements are: ")
print(a)#displaying the created matrix/array

print("type of array is:",type(a))#data type of array : type(a)

print("shape of the array:",a.shape)#shape of array : a.shape

print("size of the array is:",a.size)#size of array : a.size

#Example 1
example_1 = np.array(([1,'i',0],
                      [0,'pi',-1]))
print("type of array is:",type(example_1))#data type of array : type(example_1)
print("shape of the array:",example_1.shape)#shape of array : example_1.shape
print("size of the array is:",example_1.size)#size of array : example_1.size

#Example 2
example_2 = np.array(([1],[0]))
print("type of array is:",type(example_2))#data type of array : type(example_2)
print("shape of the array:",example_2.shape)#shape of array : example_2.shape
print("size of the array is:",example_2.size)#size of array : example_2.size

#Example 3
example_3= np.array([[1],[0]])
print("type of array is:",type(example_3))#data type of array : type(example_3)
print("shape of the array:",example_3.shape)#shape of array : example_3.shape
print("size of the array is:",example_3.size)#size of array : example_3.size