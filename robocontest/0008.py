import itertools
import collections
ls = list(map(int, input().split()))

print(list(itertools.permutations(ls, 4)))