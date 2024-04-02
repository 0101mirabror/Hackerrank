def grow(arr):
    k = 1
    for i in arr:
        k*=i
    return k


print(grow([1,2,3,4]))

'best'
# from functools import reduce

# def grow(arr):
#     return reduce(lambda x, y: x * y, arr)