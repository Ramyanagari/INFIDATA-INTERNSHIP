list1=[1,2,3,4,5,6,7,8,9,10]
even_count,odd_count=0,0
for num in list1:
    if num %2 == 0:
        even_count +=1
    else:
        odd_count +=1


print("even num in the list:",even_count)
print("odd num in the list:",odd_count)