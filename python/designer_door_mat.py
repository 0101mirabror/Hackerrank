l = list(map(int, input().split()))
N = l[0]
M = l[1] #len('WELCOME')=7 #len('.|.') = 3
c, m = 1, N-2
for i in range(1, N+1):
    if N//2+1 == i:
        print(((M-7)//2)*'-' + 'WELCOME' + ((M-7)//2)*'-')
    elif N//2 >= i:
        x = (M - len(c*'.|.'))//2
        print(x*'-' + c*'.|.' + x*'-')
        c+=2
    elif N//2 <= i:
        y = (M - len(m*'.|.'))//2
        print(y*'-' + m*'.|.' + y*'-')
        m -=2
