alp = ["", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
       "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def print_str(size):
    n = size - 1
    s = ""
    for j in range(size):
        for i in range(j):
            s += alp[i]
            s += "-"
        print(s[::-1])

def print_rangoli(size): # 3
    st = ""
    w = 4 * size - 3 # 12 - 3 = 9
    h = 2 * size - 1 #  6 - 1 = 5
    a = w // 2
    for i in range(h):
        st += a * '-'  + alp[size] + a * '-' + '\n'
    print(st)
        

print_rangoli(3)
# print_str(3)