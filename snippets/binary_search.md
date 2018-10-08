### binary_search
Trying to find given number in array of numbers. for more information on binary search visit [here](https://en.wikipedia.org/wiki/Binary_search_algorithm).

```python
def binary_search(arr, key):
    size = len(arr)
    first, second = 0, size - 1
    mid = (first + second) // 2
    while first <= second:
        if arr[mid] > key:
            second = mid - 1
        elif arr[mid] < key:
            first = mid + 1
        elif arr[mid] == key:
            print(f"found at {mid}!")
            return
        mid = (first + second) // 2
    print("not found! :(")
```

```python
binary_search([1, 2, 3, 4], 2)
```
