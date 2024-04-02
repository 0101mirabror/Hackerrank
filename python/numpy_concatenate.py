import numpy

def concat_array(NMP):
    my_array1 = []
    my_array2 = []
    for _ in range(NMP[0]):
        array1 = list(map(int, input().split()[:NMP[2]]))
        my_array1.append(array1)
    for _ in range(NMP[1]):
        array2 = list(map(int, input().split()[:NMP[2]]))
        my_array2.append(array2)
    return numpy.concatenate((my_array1, my_array2), axis=0)

if __name__ == '__main__':
    x = list(map(int, input().split()))
    print(concat_array(x))

# array1 = numpy.array([[1, 2, 3], [0, 0, 0]])
# array2 = numpy.array([[0, 0, 0], [7, 8, 9]])
 
# print(numpy.concatenate((array1, array2), axis=1))