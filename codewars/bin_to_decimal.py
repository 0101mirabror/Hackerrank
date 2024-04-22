def bin_to_decimal(inp):
    k = str(inp)[::-1]
    l = list(map(str, k))
    print(l)
    return sum([int(j)*(2**int(i)) for i, j in enumerate(l)])
print(bin_to_decimal(10))