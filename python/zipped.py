string = input().split()
col = int(string[0])
row = int(string[1])
X = []
for i in range(row):
    marks = list(map(float, input().split()))
    X+=[marks]
# print(list(zip(*X)))
for j in list(zip(*X)):
    print(round(sum(list(j))/row, 1))