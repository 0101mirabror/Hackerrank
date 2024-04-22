N, K = list(map(int, input().split()))
res = (int(N/(K-1)+N), int(N/(K-1))) if int(N/(K-1)) * K == int(N/(K-1)+N) else (int(N/(K-1)+N)-1 , int(N/(K-1))-1) 
print(res[0], res[1])