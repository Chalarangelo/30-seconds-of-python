---
title: queue_with_maximum_length
tags: list,intermediate
---

Creates a FIFO queue with maximum length.

- Creates a FIFO-based data structure in which old elements are removed when an attempt is made to include more elements than the length limit

```py
from collections import deque
def queue_with_maximum_length(lst, limit):
  return deque(lst, limit)
```

```py
a = queue_with_maximum_length([], 4)
for i in range(6):
  a.append(i)
print(a) # deque([2, 3, 4, 5], maxlen=4)
```
