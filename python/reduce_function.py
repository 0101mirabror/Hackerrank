"1"
from functools import reduce
from math import gcd #EKUB
from fractions import Fraction
# print(reduce(lambda x, y: x+y, [1,2,3,4,5], -3))
# print(reduce(gcd, [1,2,3,4,5], -3))
 

"2"
# b, c = 1, 1
# for i in range(int(input())):
#     a = list(map(int, input().split()))
#     b *= a[0]
#     c *= a[1]
# frac = Fraction(b, c)
# print(frac.denominator,frac.numerator)
'3'
def product(fracs):
    t =  reduce(lambda x, y: Fraction(x.numerator*y.numerator, x.denominator*y.denominator), fracs)
    # m =  reduce(lambda x, y: x*y, fracs)
    # print(t)
    # print(m)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
        print(fracs)
    result = product(fracs)
    print(*result)