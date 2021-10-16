---
title: find_primes
tags: math,algorithm,generator,advanced
firstSeen: 2021-10-16T20:12:37+08:00
---

Finds all prime numbers up to the given limit based on the Sieve of Eratosthenes.

- Use `yield` keyword to create an infinite sequence consists of odds.
- Use `filter()` to keep generating a new sequence filtered.
- Return a list of all prime numbers from the first prime number, 2, to the given limit.

```py
def _odd_iter():
  n = 1
  while True:
    n += 2
    yield n


def _not_divisible(n):
  return lambda x: x % n > 0


def _primes():
  yield 2
  it = _odd_iter()
  while True:
    n = next(it)
    yield n
    it = filter(_not_divisible(n), it)


def find_primes(limit):
  primes = []
  for n in _primes():
    if n <= limit:
      primes.append(n)
    else:
      break
  return primes
```

```py
find_primes(10) # [2, 3, 5, 7]
```
