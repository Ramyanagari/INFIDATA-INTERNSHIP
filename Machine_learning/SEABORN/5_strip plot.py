#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#violin plot
df=sns.load_dataset("iris")
#creating a strip plot
sns.stripplot(x='species',y='sepal_width',color='blue',data=df)
#displaying the violin plot
plt.show()