e = int(input())
s1 = set(map(int, (input().split()[:e])))
f = int(input())
s2 = set(map(int, (input().split()[:e])))

print(len(s1|s2))