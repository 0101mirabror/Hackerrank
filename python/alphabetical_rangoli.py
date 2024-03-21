alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

def print_str(size):
    n = size - 1
    s = ""
    for j in range(size):
        for i in range(j):
            s += alp[i]
            s += "-"
        print(s[::-1])


def print_rangoli(size):
    n = size - 1
    k = 2*n
    for i in range(size):
        print(k * "-" + alp[n] + k * "-")
        k-=1
        

# print_rangoli(4)
print_str(5)