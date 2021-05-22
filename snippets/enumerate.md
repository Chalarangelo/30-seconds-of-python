---
title: enumerate
tags: loops,beginner
---

Create an incrementing variable within a for loop

- Define an updating counter variable along with a for loop
- Use enumerate() to allow the counter to increment/update with each iteration

```py
def example(mylist):
  for key,value in enumerate(mylist):
    print(key)
  return 0
```

```py
example(["a","b","c"]) # 0,1,2
example([10,20,30,40,50]) # 0,1,2,3,4
```
