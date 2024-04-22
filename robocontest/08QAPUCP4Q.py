a = float(input())
for i in range(1, 11):
#   print( (format(i*a, ".2f")))
  print( format(round(i*a, 2), ".2f"), end=' ')