s1 = input()
s2 = input()
def netr(s1, s2):
    st = ''
    for i in range(len(s1)):
        if s1[i] == s2[i] == '-':
            st+='-'
        elif s1[i] == s2[i] == '+':
            st+='+'
        else:
            st+='0'
    return st
    
print(netr(s1, s2))

 