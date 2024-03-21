import numpy

a = numpy.array([1,2,3,4,5])
# print(a)          #2

b = numpy.array([1,2,3,4,5],float)
# print(b)  
def arrays(arr):
    m = list(map(int, arr))
    m.reverse()
    return numpy.array(m, float)
    pass
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')

result = arrays(arr)
print(result)
