def find_fibonacci(a=3, b=4, m=2):
    if m <= 0:
        return a
    elif m == 1:
        return b
    return find_fibonacci(m-1) + find_fibonacci(m-2)
    # elif a == 2:
    #     return 
print(find_fibonacci(a=3,b=4, m=2))