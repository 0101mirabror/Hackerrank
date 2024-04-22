N, K = list(map(int, input().split()))
c = 0
a = 1

for i in range(N * K):
    if a % K != 0:
        c += 1
    if c == N:
        break
    a+=1
print(a)

# while c < N:
#     if a%K != 0:
#         c += 1 
#     a += 1 
# print(a)
# while True:
#     if a%K != 0:
#         c += 1
#     if c == N:
#         break
#     a+=1

# print(a)