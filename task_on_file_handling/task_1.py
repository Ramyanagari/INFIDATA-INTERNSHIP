f=open("myfile1.txt",mode="r")
data=f.read()
words=data.split()
count=len(words)
print("number of words in the"
      " file:",count)