### Binary Search Implementation
Search a sorted array by repeatedly dividing the search interval in half

```python
# Returns index of x in arr if present, else -1 
def binary_search (arr, begin, end, item): 
    if end >= begin: 
        mid = begin + (end - begin)//2
        if arr[mid] == item: 
            return mid 
        elif arr[mid] > item: 
            return binary_search(arr, begin, mid-1, item) 
        else: 
            return binary_search(arr, mid+1, end, item)         
    else:          
        return -1
```

```python
arr = [3, 4, 7, 10, 19, 20]
item = 10
print(binary_search(arr,0,len(arr)-1,item))     # 3
```
