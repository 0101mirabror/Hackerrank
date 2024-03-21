def average(array):
    # your code goes here
    sum_DH = list(set(array))
    TN = len(sum_DH)
    return sum(sum_DH)/TN

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)