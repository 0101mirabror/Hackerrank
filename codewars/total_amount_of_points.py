ls = input().split()
def get_total_amount(ls):   
    s = 0
    for i in ls:
        a = list(map(int, i.split(':')))
        if a[0] > a[1]:
            s+=3
        elif a[0] < a[1]:
            s+=0
        else:
            s+=1
    return s

print(get_total_amount(ls))