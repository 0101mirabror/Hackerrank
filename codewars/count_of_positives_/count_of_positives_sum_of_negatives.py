def count_positives_sum_negatives(arr: list):
    a , b = []
    for i in arr:
        if i>0:
            a.append(i)
        elif i<0:
            b.append(i)
    if len(arr) == 0:
        return []
    return [len(a), sum(b)]