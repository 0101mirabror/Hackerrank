def find_multiples(integer,  limit  ):
    return [i for i in range(1, limit+1) if i%integer==0]

print(find_multiples(2, 10))
print(find_multiples(3, 10))
# best
# def find_multiples(integer, limit):
#     return list(range(integer, limit+1, integer))