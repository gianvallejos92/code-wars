def count_positives_sum_negatives(arr):
    if len(arr) == 0: return []

    positivesCnt = 0
    negatives = 0
    for ind in arr:
        if (ind > 0):
            positivesCnt += 1
        else:
            negatives += ind
        
    return [positivesCnt, negatives]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([1]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
print(count_positives_sum_negatives([]))
