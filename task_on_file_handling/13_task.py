f=open("hobby.txt",mode='w')
hobby=[]
for i in range(5):
    n=input("enter hobby name")
    hobby.append(n)
f.writelines(hobby)
f.close()