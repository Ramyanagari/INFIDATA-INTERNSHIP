def print_reverse_right_triangle(n):
    for i in range(n,0,-1):
        print('*' * i)


user_input=int(input("Enter the number of rows for the reverse right_angled triangle:"))

print_reverse_right_triangle(user_input)