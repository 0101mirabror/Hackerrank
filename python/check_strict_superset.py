seta = set(map(int, input().split()))
c = True
for i in range(int(input())):
    setb = set(map(int, input().split()))
    if not seta.issuperset(setb):
        c = False
if c:
    print(True)
else: 
    print(False)