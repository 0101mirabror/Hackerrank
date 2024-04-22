def mul_index(arr):
    lt = []
    for i in enumerate(arr):
        print(i)
        if i[0] == i[1] == 0:
            lt.append(i[1])
            continue
        try:
            if i[1] % i[0] == 0:
                lt.append(i[1])
        except:
            pass
    return lt
print(mul_index([22, -6, 32, 82, 9, 25]))
print(mul_index([0, 2 ,3, 6, 9]))