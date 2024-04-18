def sum(d1):
    result=[]
    for key,value in d1.items():
        result.append(key+value)
    return result

d1={1:10,2:3,4:50,5:300}
print(sum(d1))
