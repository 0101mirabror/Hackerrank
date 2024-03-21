def dec_bin(n):
    if n == 0:
        return 0 
    return n%2 + 10*(dec_bin(n//2))

def count_bits(n):
    k = str(dec_bin(n)).split('1')

    return len(k)-1
# print(dec_bin(int(input())))
print(count_bits(int(input())))
print(bin(2878))
print(dec_bin(2878))