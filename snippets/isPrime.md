---
title: functionName
tags: math,beginner
---

To check if a number is prime Number or not

```py
def isPrime(n):
  count=0
  for i in range(1,n+1):
    if n%i==0:
      count+=1
    if count==3:
      break
  if count==2:
    print("It is a Prime Number")
  else:
    print("It is not a Prime Number")
```

```py
n=71
isPrime(n)
```
