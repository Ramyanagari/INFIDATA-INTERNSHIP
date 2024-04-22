#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#box plot
#loading dataset
df=sns.load_dataset("iris")

#creating a boxplot
sns.boxplot(x='species',y='sepal_width',data=df,palette='Set2')
#displaying boxplot
plt.show()