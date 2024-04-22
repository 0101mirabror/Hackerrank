s, p = map(int, input().split())
import math
# print(s**2 - 4*p)
print(f"{-int(-s-math.sqrt(s**2-4*p))//2} {-int(-s+math.sqrt(s**2-4*p))//2}" if s**2 - 4*p >=0 else -1)
 