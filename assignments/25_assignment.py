c=12
def show():
    global c
    c=c+12
    print("inside show():",c)
show()
c=10
print("in main:",c)