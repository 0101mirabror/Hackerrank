n = int(input())
odd = list(range(1,101, 4)) + list(range(2, 101, 4))
# even = list(range(3,101, 4)) + list(range(4, 101, 4))
  
print('Azizxon' if n in sorted(odd) else 'Jahongir')
