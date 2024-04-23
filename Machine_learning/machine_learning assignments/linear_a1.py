#importing packages
import seaborn as sns #advanced visualization
import pandas as pd
import matplotlib.pyplot as plt # for basic visualization

df=pd.read_csv("exam_marks.csv")


#creating a count plot
sns.scatterplot(x="hours",y="marks",data=df)

#displaying the count plot
plt.show()