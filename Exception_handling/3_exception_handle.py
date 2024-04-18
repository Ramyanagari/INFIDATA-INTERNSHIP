a=10
b=0
try:
    div=a/b
    print("res of div:",div)
except ZeroDivisionError as e:
    print("u r trying to divide an int num by zero")
    print("e value:",e)
print("end")