---
title: deep_search
tags: list,recursion,intermediate
---

Checks the existence of a given item in a deeply nested iterable (list, tuple, set, ...).

- Uses recursion.
- Initially, the function iterates through the iterable and checks if it matches the given item.
- If it doesn't, it checks if the given object is an **iterable** by passing it to `isinstance()` along with `collections.abc.Iterable`.
- If it is an iterable, `deep_search` is called recursively with the current object as an iterable.

```py
def deep_search(iterable, item):
	for obj in iterable:
		if obj == item: return True

		if isinstance(obj, Iterable):
			if deep_search(obj, item): return True

	return False
```

```py
my_list = [[1, 2, 3], [4, 5, 6], [[7, 8, 9], [10, 11, 12], ({13, 15, 20})]]

deep_search(my_list, 15) # True
deep_search(my_list, 18) # False
```
