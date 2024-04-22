#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#violin plot
#loading dataset
df=sns.load_dataset("iris")
#creating a violin plot
sns.violinplot(x='species',y='sepal_width',data=df)
#displaying the violin plot
plt.show()