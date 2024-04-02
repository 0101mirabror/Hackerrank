import numpy
# print(numpy.eye(8, 7))
# print(numpy.eye(8, 7, k = 3))
# print(numpy.eye(8, 7, k=-1))
numpy.set_printoptions(legacy='1.13')
rows, cols = list(map(int, input().split()))

print(numpy.eye(rows, cols))
print(numpy.eye(rows, cols, k=0))
# print(numpy.identity(rows))