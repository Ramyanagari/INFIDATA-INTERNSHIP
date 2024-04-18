def mystery(num_list):
    for num in num_list:
        if num < 0:
            return False
        else:
            return True

print(mystery([3, -1, 2]))