---
title: FizzBuzz
tags: game,beginner
firstSeen: 2021-06-13T05:00:00-04:00
---

a program that prints the numbers from 1 to 50 and for multiples of `3` print `Fizz` instead of the number and for the multiples of `5` print `Buzz`. 

```py
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
```

```py
fizzbuzz
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
 ..... 
 
41
fizz
43
44
fizzbuzz
46
47
fizz
49
buzz
```
