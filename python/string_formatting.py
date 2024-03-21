def dec_bin(n):
    if n == 0 or n == 1:
        return n
    return (n%2 + 10*dec_bin(n//2))

def dec_oct(n):
    if n in [0, 1]:
        return n
    return (n%8 + 10*dec_oct(n//8))

def dec_hex_d(n):
    if n == 0 or n == 1:
        return n
    return (n%16 + 10*dec_hex_d(n//16))
    
def print_formatted(a): 
    for i in range(1, a+1):
        d = len(str(dec_bin(a))) - len(str(i)) 
        b = len(str(dec_bin(a))) - len(str(dec_bin(i)))+ 1 
        o = len(str(dec_bin(a))) - len(str(dec_oct(i)))+ 1 
        x = len(str(dec_bin(a))) - len(str(dec_hex_d(i)))+ 1 
        print(d*" " + str(i) + o*" " + str(dec_oct(i)) + x*" " + str  (dec_hex_d(i)) + b*" " + str(dec_bin(i))) 

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

    
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))