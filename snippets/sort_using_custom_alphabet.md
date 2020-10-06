---
title: sort_by_custom_alphabet
tags: sorting,lambda,utility,intermediate
---

Sort a list using custom alphabet.
- It uses lambda expression to get the index of the character in specified custom alphabet.
- Then it is passed to the `sorted` function as a key.

```py
# sort by custom alphabet
def sort_by_custom_alphabet(custom_alphabet, words):
    words = sorted(words , key= lambda word: [custom_alphabet.index(c) for c in word])
    return words

```

```py
words = ['home', 'oval', 'cat', 'egg', 'network', 'green']
custom_alphabet = 'bcdfghijklmnpqrstvwxzaeiouy'
print( sort_by_custom_alphabet (custom_alphabet,words))
```
