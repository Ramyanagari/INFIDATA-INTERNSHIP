def fibonacci_series(n):
    fib_series = [0 , 1]

    for _ in range(2,n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

user_input = int(input("Enter the number of terms for the Fibonacci series:"))
result = fibonacci_series(user_input)
print("Fibonacci series up to",user_input, "terms:",result)