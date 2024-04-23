import numpy as np#for array ops
import pandas as pd#for creating and handling dataframes

#creating dataframes from dataset
data = pd.DataFrame({'x':[-5,-4,-3,-2,-1,0,1,2,3,4,5],
                     'y':[0,0,0,0,0,0,1,1,1,1,1]})

print("dataframes",data)
print("data shape:",data.shape)

x=data['x'].values.reshape(-1,1)#choosing input values
y=data['y'].values.reshape(-1,1)#choosing output values

from sklearn.linear_model import LogisticRegression #importing algo
logistic_regressor=LogisticRegression()#initalising algorithm
logistic_regressor.fit(x,y)#training the algo on our data
print('[info] model training complete....')

#taking new output x from user
new_user_input=float(input("enter value for x:"))
#converting to array
new_user_input=[[new_user_input]]
#using the trained regression model to predict y for given x
new_output = logistic_regressor.predict(new_user_input)

#displaying results
print(f"when x ={new_user_input[0][0]},y={new_output[0]}")
