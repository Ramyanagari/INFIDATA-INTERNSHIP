import pandas as pd#used for handling dataframe

df=pd.read_csv("diabetes.csv")#loading data into a datframe
#head
print("accessing from the dataset from first 10rows\n",df.head(10))
print("accessing from the dataset from 5 rows\n",df.head())

#tail
print("accessing from the dataset from last 5rows\n",df.tail())
print("accessing from the dataset from last 10rows\n",df.tail(10))

print(df.shape)#rows and column values
print(df.columns[df.isna().any()])#to check for null values

#information data
print("basic info :\n",df.info())

#basic statistical information
print("statistical info :\n",df.describe())