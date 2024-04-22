#Displot is used basically plot distrubution of continous data
#Distribution plot
#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df=sns.load_dataset("iris")
#creating a distribution plot
sns.displot(df['sepal_width'],color='b')
#displaying the plot
plt.show()
