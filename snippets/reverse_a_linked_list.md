---
title: reverse_a_linked_list
tags: data_structure, algorithm, intermediate
---

Given a linked list, this algorithm can be used to reverse it at O(n) time-complexity and O(1) space complexity.

- reverse_a_linked_list() takes an argument called *root* which will be a head element of the linked list.
- Swap the next node of current node with the previous node.

```py
def reverse_a_linked_list(root):
  prev = None
  curr = root.head
  while curr is not None:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
  root.head = prev
```

```py
# Defination of a single node in Linked List
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

# Linked List Data Structure class
class LinkedList: 
    def __init__(self): 
        self.head = None

    # A method to add an element
    # at the beginning of the list
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # A method to print the list
    def print_list(self): 
        temp = self.head
        while(temp): 
            print (temp.data), 
            temp = temp.next

# Create a Linked List from 9 to 1
llist = LinkedList()
  for i in range(1, 10):
    llist.push(i)

# This will print the list from 9 to 1
llist.print_list()

# reverse list
reverse_a_linked_list(llist) 

# This will print the list from 1 to 9
llist.print_list()

```
