import numpy
# print(numpy.zeros((1, 2), dtype=numpy.int64))
# print(numpy.ones((1, 2), dtype=numpy.int64))
a = list(map(int, input().split()))
print(numpy.zeros(a, dtype=numpy.int8))
print(numpy.ones( a , dtype=numpy.int8))