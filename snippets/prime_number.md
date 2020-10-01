---
title: prime_number
tags: prime_number,intermediate
---

Explain briefly what the snippet does.

- Checks numbers from 2 to (given number - 1), If number is divisible by given numbers.
- Or, remainder is 0 than its a not a prime number.
- If number is prime than return 1 and otherwise return 0. 

```py
def prime_number(number):
  # code
  for other_numbers in range(2,number):
    if(number % other_numbers == 0):
        return 0
    else:
        return 1
```

```py
prime_number(21) # result
```
