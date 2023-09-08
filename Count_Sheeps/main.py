#Solution 1
def count_sheeps(sheep):
  cnt = 0
  for x in sheep:
    if x:
      cnt+=1
  return cnt

#Solution 2
def count_sheeps_2(sheep):
  return sheep.count(True)

#Test Case
print(count_sheeps_2([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))