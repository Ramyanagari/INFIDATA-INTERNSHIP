def seq(x=11,y=12):
    x=x+y
    y+=2
    print(x,'#',y)
    return x,y
a,b=seq()
print(a,'&',b)
seq(a,b)
print(a+b)
