def sum_array(arr):
  if not arr or len(arr) == 1 : return 0
  
  high = -100
  low = 1000000000
  for x in arr:
    high = max(high, x)
    low = min(low, x)
  return sum(arr) - high - low

print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([1, 1, 11, 2, 3]))
print(sum_array([6, 0, 1, 10, 10]))
print(sum_array([-6, -20, -1, -10, -12]))
print(sum_array([-6, 20, -1, 10, -12]))
print(sum_array([]))
