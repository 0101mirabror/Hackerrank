from collections import Counter
num = int(input())
room_list = (list(map(int, input().split())))
# print(sorted(room_list))
for l, i in Counter(room_list).items():
    if int(i) == 1:
        print(int(l))
# print(Counter(room_list))