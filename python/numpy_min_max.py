import numpy

def compute_min(NM: list):
    my_array = []
    for i in range(NM[0]):
        array = list(map(int, input().split()[:NM[1]]))
        my_array.append(array)
    num_min = numpy.min(my_array, axis=1)
    return numpy.max(num_min)

if __name__ == '__main__':
    x = list(map(int, input().split()))
    print(compute_min(x))
# my_array = numpy.array([[2, 5], [3,7], [1, 3], [4, 0]])
# print(numpy.min(my_array, axis=0))
# print(numpy.min(my_array, axis=1))
# print(numpy.min(my_array, axis=None))
# print(numpy.min(my_array))
# print(numpy.max(my_array, axis=0))
# print(numpy.max(my_array, axis=1))
# print(numpy.max(my_array, axis=None))
# print(numpy.max(my_array))
