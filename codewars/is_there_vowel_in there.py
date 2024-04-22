
def is_vow(inp):
    return list(map((lambda x: chr(x) if x in [97, 101, 105, 111, 117] else x), inp))
print(is_vow([105, 111, 121, 110]))