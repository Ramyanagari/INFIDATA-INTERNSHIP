A,b=5,0
try:
    A/b
except ZeroDivisionError:
    print("Hello")
except SyntaxError:
    print("hii")
except ValueError:
    print("okay")
else:
    print("bye")