import math

def is_triangular_number(number):
    test = 8 * number + 1
    square_root = math.isqrt(test)
    return square_root * square_root == test
n = int(input())
a = ''
for i in list(map(int, input().split()[:n])):
    if is_triangular_number(i):
        a+='1'
    else:
        a+='0'
print(a)