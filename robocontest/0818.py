
def floor_n(x):
    if x%1 <= 0.5 and x%1 > 0:
        return x + 0 - x%1
    elif 0.5 < x%1:
        return x + 0.5 - x%1
    return x

def ceil_n(x):
    if x%1 <= 0.5 and x%1 > 0:
        return x + 0.5 - x%1
    elif 0.5 < x%1:
        return x + 1 - x%1
    return x
print(floor_n(7))
print(ceil_n(8))



w = floor_n(sum(list(map(float, input().split())))/4)
s = floor_n(sum(list(map(float, input().split())))/4)
r = float(input())
l = float(input())
print(ceil_n(sum([r, l, w, s])/4))
