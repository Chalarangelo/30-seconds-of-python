---
title: functionName
tags: dictionary,beginner
---

snippet to invert Keys and Values In dictionary python

all keys will become values nd all values will become keys

```py
def invKeyVal(mydict):
    inv_dict = {v:k for k, v in my_dict.items()}
    return inv_dict
```

```py
my_dict={1:'Python',2:'JavaScript',3:'PHP'}
my_dict=invKeyVal(my_dict);
print(my_dict)
```
