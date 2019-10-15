---
title: swap_case
tags: string, begginer
---

Swaps the case of the string 's'.
Checks for the case of the character of the string and accordingly updates it and appends to another string 'a'.
Then returns string 'a'.

```py
def swap_case(s):
	a = ""
	for let in s:
		if let.isupper() == True:
			a+=(let.lower())
		else:
			a+=(let.upper())
	return a
```