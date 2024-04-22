n = int(input())
print('Error' if (n < 1 or n > 12) else 'Spring' if 3<=n<=5 else 'Summer' if 6<=n<=8 else 'Autumn' if 9<=n<=11  else 'Winter')