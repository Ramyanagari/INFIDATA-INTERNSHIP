a=10
b=10
l1=[2,3,4,5]
try:
    print("list element is:", l1[4])
    div = a / b
    print("res of div:", div)
except ZeroDivisionError as e:
    print("u r trying to divide an int num by zero")
    print("e value:", e)
except Exception as e:
    print("your are at generalised Exception block")
    print("e value:",e)
print("end")