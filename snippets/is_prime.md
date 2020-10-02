---
title: is_prime
tags:  math,beginner
---
Check Number is prime or not.

- Check numbers from 2 to the given number, If given number is divisible by numbers.
- Or, remainder is 0 than its a not a prime number.
- If number is not prime than return 0 and otherwise return 1. 

```py
def is_prime(number):
  for other_numbers in range(2,number):
    if(number % other_numbers == 0):
      return 0
      break
  else:
    return 1
```

```py
is_prime(21)
```
