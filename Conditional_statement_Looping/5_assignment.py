bike_price=int(input("bike_price"))
print("the road tax you should pay is")
if bike_price>100000:
    val=bike_price*0.15
    print("the road tax is:",val)
elif bike_price>50000 and bike_price<=100000:
    val2=bike_price*0.1
    print("the road tax is:",val2)
elif bike_price<=50000 and bike_price>=0:
    val3=bike_price*0.5
    print("the road tax is:",val3)
else:
    print("unknow")