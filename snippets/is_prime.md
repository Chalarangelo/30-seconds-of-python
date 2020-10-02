---
title: is_prim
tags:  math,beginner
---

- Check numbers from 2 to the given number, If given number is divisible by numbers.
- Or, remainder is 0 than its a not a prime number.
- If number is prime than print "Prime Number" and otherwise print "Not a prime number". 

```py
def is_prime(number):
  for other_numbers in range(2,number):
    if(number % other_numbers == 0):
        print("not a prime number")
        break
  else:
    print("Prime number")
```

```py
is_prime(21)
```
