---
title: bin_to_dec
tags: math, beginner
---

Returns the decimal representation of a given binary number.

- Use the `int()` function to convert a given binary number into its decimal representation.

```py
def bin_to_dec(num):
	return int(f'0b{num}', 2)
```

```py
bin_to_dec(101010) # 42
bin_to_dec(1010) # 10
```