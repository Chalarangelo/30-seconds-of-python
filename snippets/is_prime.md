---
title: is_prime
tags:  math,beginner
---
Check Number is prime or not.

- Check numbers from 2 to the given number, If given number is divisible by numbers.
- Or, remainder is 0 than its a not a prime number.
- If number is not prime than return 0 and otherwise return 1. 

```py
from math import sqrt

def is_prime(number):
  if(number % 2 == 0 and number > 2):
    return False
  for other_numbers in range(3,sqrt(number)+1,2):
    if(number % other_numbers == 0):
      return False
  return True
```

```py
is_prime(21) #result
```
