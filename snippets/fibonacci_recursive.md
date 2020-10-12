---
title: fibonacci_recursive
tags: recursive,intermediate
---

Returns a list of Fibonacci Sequence containing <i>n</i> numbers.

- Fibonacci Sequence generator using Recursive method.
- Throws error when <i>n</i> is not int or is less than 0.


```py
def main(n):
	def fibonacci_rec(i):
		if i < 2:
			return i	
		else:
			return fibonacci_rec(i-1) + fibonacci_rec(i-2)

	fibonacci_list = []
	for i in range(n):
		fibonacci_list.append(fibonacci_rec(i))
	return fibonacci_list
```

```py
main(10) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
