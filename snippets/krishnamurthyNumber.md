---
title: checkKrishnaMurthyNumber
tags: math,intermediate
---
- A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself.
- Checks if the given number is KrishnaMurthy number or not. If it is a KrishnaMurthy number the function returns True else False.

```py
def factorial(num):
	if num == 0:
		return 1
	return num * factorial(num-1)

def checkKrishnaMurthyNumber(n):
	temp = n
	s = 0 
	while n > 0:
		mod = n % 10
		s += factorial(mod)
		n = n//10
	if s == temp:
		return True
	else:
		return False
```

```py
checkKrishnaMurthyNumber(145) #True
checkKrishnaMurthyNumber(40585) #True
checkKrishnaMurthyNumber(152) #False
```
