def display_words():
    f= open("story.txt","r")
    data = f.read()
    words = data.split()
    for i in words:
        if len(i)<4:
            print(i, end=",")
        f.close()

display_words()