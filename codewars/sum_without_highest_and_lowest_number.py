def sum_array(arr: list):
    if arr == None or len(arr)==(1 or 0):
        return 0
    arr.remove(min(arr))
    arr.remove(max(arr))
    return sum(arr)
 
print(sum_array( [1, 1, 11, 2, 3]))

# best practice

# def sum_array(arr):
#     if arr == None or len(arr) < 3:
#         return 0
#     return sum(arr) - max(arr) - min(arr)