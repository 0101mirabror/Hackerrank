from collections import  Counter
a = dict(Counter(input()))
# print(a)
if len(a.values())%2 ==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
