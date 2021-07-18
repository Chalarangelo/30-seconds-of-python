---
title: word_count
tags: string,beginner
firstSeen: 2021-07-18T08:14:11+0000
lastUpdated: 2021-07-18T08:14:11+0000
---

Calculates the total number of occurence of a word in a given string .

- Uses `.split()` method to give a list of words from the string, which is used to find the total occurence of a word in that list using a counter `count`

```py
def word_count(query, string):
  words = string.split()
  count = 0

  for word in words:
    if word == query:
      count += 1

  return count
```

```py
string = "cup infront of a cup behind another cup"
word = "cup"

def word_count(word, string) # 3
```
