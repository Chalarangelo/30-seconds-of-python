### quicksort

Quicksort is an example of a "divide-and-conquer" algorithm, where we solve the problem
by dividing it to smaller subproblems.
We pick the first element of the list (although it can be a random element) as a "pivot".
We then recursively sort two smaller problems: all elements less than or equal to the pivot,
and all elements that are greater than the pivot. All that's left is to connect the sublists
together with the pivot.

```py
def quicksort(lst):
    if not lst:
        return []
    pivot = lst[0]
    less_than_or_equal = [x for x in lst[1:] if x <= pivot]
    greater_than = [x for x in lst[1:] if x > pivot]
    return quicksort(less_than_or_equal) + [pivot] + quicksort(greater_than)
```

```py
lst = [7,4,9,2,6,3]
quicksort(lst) # sorted [2, 3, 4, 6, 7, 9]
```