def triangular_number(index):
    return (index*(index+1))//2
st = ''
n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()[:2]))
    if triangular_number(a) == b:
        st += '1'
    else:
        st += '0'
print(st)