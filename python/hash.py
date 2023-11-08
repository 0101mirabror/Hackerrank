n = int(input())
h = str(input())
k = h.split()
l = tuple(map(int, k))
print(l)
print(hash(l))
# hash_tuple = [str(input()) for _ in range(n)]