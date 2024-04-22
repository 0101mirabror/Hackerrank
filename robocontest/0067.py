n = int(input())
print(n)
k = bin(n)[2:] if n >=0 else bin(n)[3:]
t = (32-len(k))*'0' + k
print(type(t))
print(t if n>=0 else ''.join(list(map(lambda x: eval(x+"-"+'1') if x == "1" else eval(x+"+"+'1'), t))))