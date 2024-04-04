def merge_array(arr1, arr2):
    return sorted(list(set(arr1 + arr2)))
print(merge_array([1, 3, 5, 7, 9, 11, 12], [-1, 2, 3, -4, 5, 10, 12]))
print(merge_array([0, 35, 36, 37, 6, 7, 8, 9, 10, 38, -20, 39, 40, 50, -10, 25, -5, 62], [12, 23]))