def mystery(num_list):
    index = 0
    while index < len(num_list):
        num = num_list[index]
        if num == 0:
            num_list.pop(index)
        index +=1
        
list1 = [3, 0, 2, 0, 0]
mystery(list1)
print(list1)