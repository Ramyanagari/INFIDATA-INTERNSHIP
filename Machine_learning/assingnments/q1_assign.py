#creating a dataframe?dataset

import pandas as pd
#how to convert dictionary to dataframe
from datetime import datetime

data=pd.DataFrame({
    "name":["Alice","Bob","charlie"],
    "age":[25,30,35],
    "city":["Newyork","Los Angeles","Chicago"]
})
print(data)

#saving the dataframe created as csv file
data.to_csv('person_info.csv',index=False)

print("shape of the dataframe:\n",data.shape)#displays shape of dataset

print("size of the dataframe is:\n",data.size)#display size of data

age=data['age'].describe() # using.describe()
print(age)

#data manipulation
year=datetime.now().year
data['year of birth']=year-data['age']
filtered_data=data[data['age']>30]
filtered_data.to_csv("filtered_person_info.csv",index=False)
