import numpy

# arr = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# transpose_arr = numpy.transpose(arr)
# print(transpose_arr)

# flatten_arr = transpose_arr.flatten()
# print(flatten_arr)
rows, cols  = list(map(int, input().split()[:2]))
ls = [list(map(int, input().split()[:cols])) for _ in range(rows)]
arr = numpy.array(ls)
print(numpy.transpose(arr))
print(arr.flatten())