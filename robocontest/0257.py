n = input()
k = n.count('1')
print('Yes' if n.count(k*'1') == 1 else 'No')