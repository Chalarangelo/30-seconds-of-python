---
title: for-else loop
tags: loop,searchig,beginnner
---

The else clause of for-loop helps us direct the flow of code execution based on the outcome of the loop.

- Run the for loop on an iterable data such as list. 
- If the loop finds what it was looking for and break statement is encountered, the else part of the loop is ignored.
- If the loop doesn't find it, else part is executed.

```py

#EXAMPLE CODE

for item in container:
  if search_something(item):
    # Found it!
    process(item)
    break
else:
  # Didn't find anything..
  not_found_in_container()

```

```py
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print( n, 'is not a prime number')
        break
  else:
    # loop fell through without finding a factor
      print(n, 'is a prime number')
```



```py
2 is a prime number
3 is a prime number
4 is not a prime number
5 is a prime number
6 is not a prime number
7 is a prime number
8 is not a prime number
9 is not a prime number
```
