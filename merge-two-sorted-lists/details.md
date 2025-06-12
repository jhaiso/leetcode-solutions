# 21. Merge Two Sorted Lists

## Relevant Topics

Linked List, Recursion

## Solution Thought Process

### Iteration

We keep two pointers to the current positions of each list. We iteratively compare the two, and splice the lists together.

```python
# initialize a dummy and current node #dummy keeps track of the head of the sorted list

# while both list nodes exist
#   if value of list 1 < value of list 2
#       set the next of current to list1
#       increment the list1 pointer
#   otherwise
#       set the next of current to list2
#       increment the list2 pointer
#   set curr to curr.next (the recently appended node)
# append the remainder of the list

# return the dummy
```

### Recursion
Base cases: when one of the lists is empty, we return the other one
If the value of list1 is less than value of list2, then we recursively call the function on list1.next.
