---
title: csv_to_list
tags: utility,csv,list,beginner
---

Converts a line of CSV text to Python list.

- `csv_to_list()` returns Python list converted from CSV text.
- `csv.reader` object parses CSV text and appends each element to the output list.
- The input must be a line of CSV text.
- Quoted texts are handled properly.

```py
import csv

def csv_to_list(csv_text):
  result = []
  for elem in csv.reader((csv_text, )):
    result += elem
  return result
```

```py
csv_to_list('123,"Quoted, sample text",456') # ['123', 'Quoted, sample text', '456']
```
