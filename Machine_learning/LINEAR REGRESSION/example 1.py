import numpy as np#for array operations
import pandas as pd#for creating and handling dataframes

example1_data = pd.DataFrame({'x':[0,1,2,3,4],
                              'y':[1,2,3,4,5]})
print(example1_data)#displaying example 1 dataframe

x=example1_data['x'].values.reshape(-1,1)#choosing input values
y=example1_data['y'].values.reshape(-1,1)#choosing ouput values

from sklearn.linear_model import LinearRegression#importing algo
linear_regressor = LinearRegression()#initalising algorithm
linear_regressor.fit(x,y)#training the algo on our data
print('[info] linear regression model training complete...')

m=linear_regressor.coef_[0][0]
c=linear_regressor.intercept_[0]

print(f"m value is:{m}")
print(f"c value is:{c}")
print(f"equation of line is:y{m}x+{c}")

new_user_input = float(input("enter value of x:"))
new_user_input = [[new_user_input]]
new_output = linear_regressor.predict(new_user_input)[0]
print(f"when x = {new_user_input},y={new_output}")