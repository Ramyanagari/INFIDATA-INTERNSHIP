def largest(list):
    large=list[0]
    for i in list:
        if i>large:
            large=i
    return large

list=[1,2,3,4,5,6,7,8,9,10]
print("largest in",list,"is")
print(largest(list))