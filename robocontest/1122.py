n = int(input())
print('YES' if len(str(n))%2==1 and len([i for i in str(n) if int(i)%2==0])==0 else "NO")