f=open("myfile1.txt",mode='r')

data =f.readlines()
print("data is:",data)

for i in data:
    print(i)

for i in data:
    word=i.split()   #whenever space comes it will split as a word
    print(word)