def mystery(num_list):
    out = []
    for num in num_list:
        if num > 10:
            out.append(num)
    return out

print(mystery([5, 10, 15, 20]))