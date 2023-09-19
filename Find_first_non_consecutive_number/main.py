def first_non_consecutive(arr):
    if (len(arr) < 2): return None
    for ind in range(1, len(arr)):
        if (arr[ind-1] + 1 != arr[ind]):
            return arr[ind]
    return None

print(first_non_consecutive([1,2,3,4,6,7,8]))
print(first_non_consecutive([1,2,3,4,5,6,7,8]))
print(first_non_consecutive([4,6,7,8,9,11]))
print(first_non_consecutive([4,5,6,7,8,9,11]))
print(first_non_consecutive([31,32]))
print(first_non_consecutive([-3,-2,0,1]))
print(first_non_consecutive([-5,-4,-3,-1]))
print(first_non_consecutive([]))
print(first_non_consecutive([5]))
print(first_non_consecutive([3,5]))