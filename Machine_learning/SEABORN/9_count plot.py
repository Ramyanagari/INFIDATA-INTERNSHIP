#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#countplot
df=sns.load_dataset("iris")
#creating a countplot
sns.countplot(x='sepal_length',hue='species',data=df,palette='Set2')
#displaying the plot
plt.show()