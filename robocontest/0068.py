n = int(input())
ls = set(map(int, input().split()[:n]))
k = int(input())

print(sorted(list(ls))[k-1])