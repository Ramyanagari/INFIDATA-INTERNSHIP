try:
    A=9.99999999/5
except(ArithmeticError,IOError) as e:
    print(e)
else:
    print(A)