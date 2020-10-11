---
title: csv_to_json
tags: utility,csv,json,beginner
---

Converts a comma-separated values (CSV) file to JSON. The first row of the file is used as the title row.

- `csv_to_json` function takes CSV file path as input and returns JSON data.
- `csv.DictReader` parses input CSV file and iterating over it returns each row, in a key-value pair form.
- `csv_file` parameter should be a valid CSV file path, you can also give absolute or relative file path.

```py
import csv
def csv_to_json(csv_file):
  json_data = []
  with open(csv_file) as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
      json_data.append(row)
  return json_data
```

```py
csv_to_json('superheros.csv') # [{'Superhero': 'Iron Man', 'Comic book': 'Marvel'}, {'Superhero': 'Batman', 'Comic book': 'DC'}, {'Superhero': 'Arrow', 'Comic book': 'DC'}]
```