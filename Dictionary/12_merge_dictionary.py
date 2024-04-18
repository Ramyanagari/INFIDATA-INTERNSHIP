def merge(dict1,dict2):
    return dict1.update(dict2)

d1={1:10, 2:20, 3:30, 4:40}
d2={2:20, 3:30, 6:60, 7:70}
merge(d1,d2)
print("update d1 is:",d1)


