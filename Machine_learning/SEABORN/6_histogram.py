#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
data=sns.load_dataset("iris")
#creating a histogram plot
sns.histplot(x='species',y='sepal_width',data=data)
#displaying the histogram plot
plt.show()