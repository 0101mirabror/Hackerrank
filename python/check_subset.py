 
for i in range(int(input())): 
    seta_num = int(input())
    seta = set(map(int, input().split()[:seta_num]))
    setb_num = int(input())
    setb = set(map(int, input().split()[:setb_num]))
    if seta.issubset(setb):
        print(True)
    else:
        print(False)
        