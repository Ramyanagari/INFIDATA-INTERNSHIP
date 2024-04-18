a=10
b=10
l1=[2,3,4,5]
try:
    print("list element is:",l1[4])
    div=a/b
    print("res of div:",div)
except ZeroDivisionError as e:
    print("u r trying to divide an list num by zero")
    print("e value:",e)
except Exception as e:
    print("am at generalised exception block")
    print("e value:",e)
finally:#finally block always executes
    print("am at finally block")
    print("executing at finally")
print("end")