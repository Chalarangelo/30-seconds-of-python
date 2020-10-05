---
title: reverse_list
tags: list,beginner
---

Returns the reverse of a list.

- [::-1] starts from the end of the list moving towards the first element taking each element. So it reverses the list

```py
def reverse_list(lst):
  return lst[::-1]
```

```py
reverse_list([1,2,3,4,5]) #[5,4,3,2,1]
reverse_list(['a','b','c','d']) #['d','c','b','a']
```
