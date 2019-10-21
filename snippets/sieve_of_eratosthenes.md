---
title: sieve_of_eratosthenes
tags: math,intermediate
---

Generate Prime numbers upto n

First we create a list of all numbers from 2 to n. Then we mark all the numbers which are divisable by 2 and are `>=` square of it. Then we take next unmarked number 3 we mark all multiples of 3 same as 2. then we move to next unmarked number 5. We continue this procedure until we processed all numbers in list.
finally the unmarked ones are our prime numbers.
Time complexity : O(n\*log(log(n)))

```py
def sieve_of_eratosthenes(num):
    
    primes = [True for i in range(num + 1)]
    p = 2
    
    while p * p <= num:
        if primes[p] == True:
            for i in range(p*p, num+1, p):
                primes[i] = False
        p+=1

    for prime in range(2, num+1):
        if primes[prime]:
            print(prime, end=" ")
```

```py
sieve_of_eratosthenes(10) # 2 3 5 7
```