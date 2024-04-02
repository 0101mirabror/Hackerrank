def sum_of_differences(arr: list):
    arr.sort(reverse=True)
    c  = 0
    if len(arr) == 0 or len(arr)==1:
        return None
    for i in range(len(arr)):
        print(i)
        c+=arr[i]-arr[i+1]
        if i == len(arr)-2:
            break
    return c
print(sum_of_differences([2, 1 , 5,10]))