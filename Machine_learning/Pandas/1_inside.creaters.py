#CREATING A DATAFRAME/DATASET

import pandas as pd
#how to convert dictionary to dataframe

data=pd.DataFrame({
    "name":["ali","khan","mahesh","vinit"],
    "age":[20,25,30,25],
    "branch":["cse",",me","ise","ece"],
    "place":["bangalore","delhi","mysore","porbander"]
})
print(data)

#saving the dataframes created csv file
data.to_csv('id.csv',index=False)