from itertools import product
# k = list(product([1,2,3], [5,2,3,6]))
# print(k)
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
# k =   set(product(a, b))
for i in list(product(a, b)):
    print(i, end=" ")
# print(k)