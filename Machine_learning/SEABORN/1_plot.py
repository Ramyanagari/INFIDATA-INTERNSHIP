#importing packages
import seaborn as sns#advanced visualization
import matplotlib.pyplot as plt#for basic visualization

#loading dataset
df = sns.load_dataset("iris")#loading the dataset
print(df)#displaying the dataset

#draw lineplot
sns.lineplot(x="sepal_length",y="sepal_width",data=df)
#setting the title using Matplotlib Function
plt.title('Title using Matplotlib Function')
plt.show()#displaying the plot