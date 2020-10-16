---
title: to_hash
tags: math,beginner
---

Returns the hash representation of the given string.

- Use `hashlib` to convert a given string into its hash equivalent.

```py
from hashlib import *

def toMD5(string):
	return md5(string.encode()).hexdigest()

def toSHA1(string):
	return sha1(string.encode()).hexdigest()

def toSHA256(string):
	return sha256(string.encode()).hexdigest()

```

```py
toMD5("python") # 23eeeb4347bdd26bfc6b7ee9a3b755dd
toSHA1("python") # 4235227b51436ad86d07c7cf5d69bda2644984de
toSHA256("python") # 11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1
```
