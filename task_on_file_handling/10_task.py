def count_words():
    f= open("notes.txt","r")
    count = 0
    data = f.read()
    words = data.split()
    for i in words:
        count+=1
    print("Total words are",count)
    f.close()

count_words()