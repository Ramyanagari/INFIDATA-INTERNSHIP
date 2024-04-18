#ASSUMING A DATAFRAME/DATASET IS ALREADY PRESENT,
#THIS IS HOW WE READ/LOAD IT

import pandas as pd#for creating and handling dataframes
#loading id.csv into pandas dataframe
data=pd.read_csv("diabetes.csv")
print(data)#displaying the dataframe

#
print("display specfic columns")
print(data['Glucose'])#displaying single column
print(data[["Glucose","BMI"]])#displaying multiple column
#
print(data.shape)#displaying multiple column

print(data.shape)#displays size of dataset

print(data.size)#displays size of data

#INDEXING
print(data.head())#print first 5 rows of data
print(data.head())#print first 5 rows of data