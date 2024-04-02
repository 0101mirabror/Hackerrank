import sys

# print(sys.getsizeof((1, 2)))
# print(sys.getsizeof([1, 2]))
# print(sys.getsizeof((1)))
# print(sys.getsizeof("Hello"))
# print(sys.getsizeof("龘"))
import sys
def total_bytes(obj):
    return sys.getsizeof(obj)

# from sys import getsizeof as total_bytes