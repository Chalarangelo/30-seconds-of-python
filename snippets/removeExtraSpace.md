---
title: removeExtraSpace
tags: string,replace
---

Return the string without extra space 

- Replace all the double space in the given string till double space "  " is not present in the given string.
- Use `str.replace()` to replace the double spaces with single space.

```py
def removeExtraSpace(string):
	while '  ' in string:
		string = string.replace('  ',' ')
	return string
```

```py
print(removeExtraSpace('Python     is a    strong    programming      language')) #Python is a strong programming language
```
