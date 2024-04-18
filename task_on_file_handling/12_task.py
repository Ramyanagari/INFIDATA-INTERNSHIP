f=open("name.txt",mode='w')


for i in range(5):
    n=input("enter name")
    f.write(n)
f.close()