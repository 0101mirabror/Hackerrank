import numpy

n = int(input())
C =  []
for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    C.append(a + b)
# print(C)
# A = numpy.array(C[0])
# B = numpy.array(C[1])
print(numpy.cross([1, 2], [3, 4]))
 