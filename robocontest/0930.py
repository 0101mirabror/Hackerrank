for _ in range(int(input())):
  i = int(input())
  f = 2**i + 3**i + 5**i + 6**i
  print('YES' if int(f**(1/3))**3 == f else 'NO' )