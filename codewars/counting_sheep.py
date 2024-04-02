def count_sheeps(sheep):
  c = 0
  for i in sheep:
    if i == True:
      c+=1
  return c
# print(count_sheeps())
# best
# def count_sheeps(arrayOfSheeps):
#   return arrayOfSheeps.count(True)