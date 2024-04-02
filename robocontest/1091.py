a, b, c = list(map(int, input().split()))
if a == b and b == c:
    print(1)
elif ((a == b or a == c) and b != c) or ((b == c or b == a) and a!=c) :
    print(2)
else:
    print(3)