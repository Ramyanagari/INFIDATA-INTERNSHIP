def line_count():
    f = open("story.txt","r")
    count=0
    for i in f:
              count+=1
    f.close()
    print("No of lines not starting with 'T'=",count)

line_count()