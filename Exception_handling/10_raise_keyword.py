try:
    raise ZeroDivisionError("demo message")
except ZeroDivisionError as e:
    print("am at ZeroDivision block")
    print("e value:",e)