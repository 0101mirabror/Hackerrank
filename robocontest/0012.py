n = int(input())
def is_prime(a):
    c = 0
    for i in range(2, a+1): 
        if a%i == 0:
            c += 1
            if c > 1:
                break
    return c == 1

def prime_nums(a):
    c = []
    for i in range(2, a+1): 
        if is_prime(i):
            c.append(i)
    return 'Bobur' if len(c)%2==0 else 'Ali'
print(prime_nums(n))
