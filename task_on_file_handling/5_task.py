f=open("myfile1.txt",mode='r')


count=0

for i in f:
    words = i.split()
    count=count+1
print("the number of lines",count)