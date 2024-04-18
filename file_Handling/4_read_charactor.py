f=open("myfile1.txt",mode='r')

data1=f.read(7)
print("data1 is:",data1)

data2 =f.read(8)
print("data2 is:",data2)

f.close()