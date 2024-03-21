n = int(input())
line1 = set(map(int, input().split()[:n]))
k = int(input())
line2 = set(map(int, input().split()[:k]))
for i in sorted(list(line1.symmetric_difference(line2))):
    print(i)
print(sorted(list(line1.difference(line2).union(line2.difference(line1)))))
print(sorted(list(line1.symmetric_difference(line2))) == sorted(list(line1.difference(line2).union(line2.difference(line1)))))