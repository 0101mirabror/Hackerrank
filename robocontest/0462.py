n = input()
alp = {
    'hS': 'Sh', 'hC':'Ch', 'gN': 'ng',
    'hs': 'sh', 'hc': 'ch', 'gn': 'ng'
}

new_n = n[::-1]
for i in alp.keys():
    if i in new_n:
        new_n = new_n.replace(i, alp[i])
print(new_n)
