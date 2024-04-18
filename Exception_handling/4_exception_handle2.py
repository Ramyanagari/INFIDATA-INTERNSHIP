l1=[2,3,4]
try:
    print(l1[3])
except IndexError as e:
    print("your trying to access the wrong index ")
    print("e value:",e)
print("end")