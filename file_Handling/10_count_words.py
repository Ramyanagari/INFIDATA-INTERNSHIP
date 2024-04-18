f=open("myfile1.txt",mode='r')

count=0


for i in f:
    word=i.split()
    count=count+1
print("number of words in file:",count)


f=open("myfile1.txt",mode='r')
data=f.read()
words=data.split()
count=len(words)