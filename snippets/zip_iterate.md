---
title: zip_iterate
tags: list, beginner
---

Snippet demonstrates how `zip` functions allow for iterating through multiple iterables.

- This example iterates through two lists and executes the provided `fn` for every element. 


```py
def zip_iterate(list_one, list_two, fn): 
  for (a, b) in zip(list_one, list_two): 
  	fn(a, b)
```

```py
zip_iterate(['a', 'b', 'c'], [1, 2, 3], print) #a 1 b 2 c 3
```
