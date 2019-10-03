---
title: remove_punctuation
tags: string, regex, beginners
---
Remove punctuation using regular expresions. The module `re` provide us of several methods to apply regex to manipulate string. 
`sub` method replaces the pattern matches for another string. 
The `[^\w\s]` pattern will match any character that is neither a number or alphabetic character (i.e. punctuation).

```py
from re import sub, compile
pattern = compile(r'[^\w\s]')
def remove_punctuation(s:str):
    return sub(pattern, '', s)
print(remove_punctuation('Hi, my name is Adan and I am 21 years old.'))
# Output: Hi my name is Adan and I am 21 years old
```

This is useful for text cleaning and data cleaning.
