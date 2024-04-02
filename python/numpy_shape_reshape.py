import numpy

# arr = numpy.array(([1, 2, 3, 13, 9, 2, 1, 2, 6]))
# print(arr.shape)
# arr.shape = (3, 3)
# print(arr, arr.shape)
# new_arr = numpy.reshape(arr, (9,))
# print(new_arr)
arr = list(map(int, input().split()[:9]))
new_arr = numpy.reshape(arr, (3,3))
print(new_arr)