from functools import reduce
import operator
def find_difference(a,b):
    return abs(reduce(operator.mul, a) - reduce(operator.mul, b))
print(find_difference([3, 2, 5], [1, 2, 4]))