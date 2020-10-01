
---
title: Split String to a list of substrings
tags: object,strings,intermediate
---
This snippet helps you to spit a long string to short list of substrings.
- Adding a string `mystring = "My name is 30 seconds of Python"`
- We can seperatae it by the property. `.split()`
- `''`  Space is the default seperator
-  We can add seperator by ourselves. To make a seperator `/` just edit the split property `.split('/')`

```python
mystring = "My name is 30 seconds of Python"
mystring_2 = "sample/ string "
```

```python
# default separator ''
print(mystring.split())
# returns ['My', 'name', 'is', '30', 'seconds', 'of', 'Python']

# custom seperator /
print(mystring_2.split('/'))
# returns ['sample', ' string 2']
```