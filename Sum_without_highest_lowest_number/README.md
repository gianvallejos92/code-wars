# Sum without highest and lowest number
[Link: Sum without highest and lowest number - CodeWars](https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python)

Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

## Input
``` batch
[6, 2, 1, 8, 10]
[1, 1, 11, 2, 3]
[6, 0, 1, 10, 10]
[-6, -20, -1, -10, -12]
[-6, 20, -1, 10, -12]
```

## Output
``` batch
16
6
17
-28
3
```

## Input Validation
If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
