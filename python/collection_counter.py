from collections import Counter
X = int(input())
size_sh = list(map(int, input().split()[:X]))
print(size_sh)
a = Counter(size_sh)
print(a, "A")
N = int(input())
x = {}
sum = 0
for i in range(N):
    data = list(map(int, input().split()))
    x[data[0]] = data[1]
    if data[0] in a.keys() and a[data[0]] > 0:
        sum+=data[1]
        a[data[0]]-=1
print(sum)
# b = Counter(x.keys())
# print(b)
# for i in b:
#     if i in a.keys
