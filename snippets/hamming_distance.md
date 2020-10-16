---
title: hammingDistance
tags: math,basic
---

- The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Example:<br>
1 1 0 1 1 1 0 0 - 220 <br>
1 1 1 1 0 1 1 0 - 246<br>
Number of change in bits between the two numbers in binary is 3. Hence, hamming distance is 3.

```py
def hammingDistance(x,y):
	return bin(x^y).count('1')
```

```py
hammingDistance(220,246) #3
hammingDistance(4,8) #2
hammingDistance(1,4) #2
```
