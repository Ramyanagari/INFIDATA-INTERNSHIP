def count_hash():
    f= open("matter.txt","r")
    data = f.read()
    for i in data:
        print(i, end="#")

    f.close()

count_hash()    