def dec_bin(n):
    if n == 1: 
        return 1
    return n%2 + 10*dec_bin(n//2)
print(dec_bin(10))
sr = input()

print(len(sr))
for i in sr:
    k = ord(i)
    print(dec_bin(k))
