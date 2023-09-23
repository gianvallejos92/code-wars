# Count characters in your string
[Link: Count characters in your string - CodeWars](https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python)

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

## Input
```batch
count('aba')
count('')
count('aa')
count('aabb')
```

## Output
```batch
{'a': 2, 'b': 1}
{}
{'a' : 2}
{'b' : 2, 'a' : 2}
```
