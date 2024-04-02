import numpy

NM = list(map(int, input().split()))
my_array = []
for i in range(NM[0]):
    array = list(map(int, input().split()[:NM[1]]))
    my_array.append(array)
print(my_array)
num_sum = numpy.sum(my_array, axis=0)
print(num_sum)
num_prod = numpy.prod(num_sum, axis=0)
print(num_prod)


# my_array = numpy.array(([1, 2, 10], [3, 4, 11], [5, 6, 12]))
# print(numpy.sum(my_array, axis=0))
# print(numpy.sum(my_array, axis=1))
# print(numpy.sum(my_array, axis=None))
# print(numpy.sum(my_array))
# print(numpy.prod(my_array, axis=0))
# print(numpy.prod(my_array, axis=1))
# print(numpy.prod([4,6], axis=None))
# print(numpy.prod(my_array))