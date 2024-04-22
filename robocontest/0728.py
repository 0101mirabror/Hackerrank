a, b  = list(map(int, input().split()))
print(a if (a//b+1)*b == a  else (a//b+1)*b)