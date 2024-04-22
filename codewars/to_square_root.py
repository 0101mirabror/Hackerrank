# import math
# def square_or_square_root(arr):
#     return list(map(lambda x: int(math.sqrt(x)) if math.sqrt(x) % 1 == 0 else x**2, arr ))
import math
square_or_square_root=lambda arr: [int(math.sqrt(x)) if math.sqrt(x) % 1 == 0 else x**2 for x in arr]
print(square_or_square_root([4,3,9,7,2,1]))
print(type(square_or_square_root))