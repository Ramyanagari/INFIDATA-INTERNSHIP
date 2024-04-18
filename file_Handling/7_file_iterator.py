f=open("myfile1.txt",mode='r')
data1=f.readline()

for i in data1:
    print(i)

for i in f:
    print(i)