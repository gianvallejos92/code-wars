def count(s):
  res = dict()
  for x in s:
    if x in res:
      res[x] = res[x] + 1
    else:
      res[x] = 1
  return res

print(count("aba"))
print(count(""))
print(count("aa"))
print(count("aabb"))
