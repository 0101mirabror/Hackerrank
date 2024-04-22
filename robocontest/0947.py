
n = int(input())
m = list(set(map(int, input().split()[:5])))
m.sort()
print(m[::-1][2] if len(m)>=3 else m[-1])
