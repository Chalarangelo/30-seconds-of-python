---
title: csv_reader
tags: file, beginner
---

Extracts the data from csv file.

Use `open()` to open the file and `csv.reader()` to read the file

```py
import csv

def read_csv(filename):
  csv_content = [row for row in csv.reader(open(filename, 'r'))]
  return csv_content[1:]
```

```py
read_csv("<filename>.csv") # Contents of csv file
```
