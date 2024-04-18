print("function demo")
def addition(*num):
    result=num[0]+num[1]
    print("addition of {0} and {1} is {2}". format(num[0],num[1],result))

print("function with orbitary arguments")
addition(15,20)
