def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)
    return factorial
print("function with return parameter example")
n=int(input("enter the number:"))

fact=factorial(n)
print("factorial of a number is:",fact)