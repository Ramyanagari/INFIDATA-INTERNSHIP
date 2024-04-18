f=open("myfile2.txt",mode="w")
l1=["web program\n","java program\n","python program\n"]

f.write("welcome to programming\n")
f.writelines(l1)
f.close()