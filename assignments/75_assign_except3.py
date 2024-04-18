a=6.5
try:
    print(a)
except NameError:
    print("Variable not defined")
except ValueError:
    print("the value must be an integer")