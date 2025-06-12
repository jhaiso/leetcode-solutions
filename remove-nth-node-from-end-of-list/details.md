# 19. Remove Nth Node From End of List

## Relevant Topics

Linked List, Two Pointers

## Solution Thought Process

### Two Pointers

Initialize a dummy node pointing to the head. Set the left pointer to that dummy, and the right pointer to the head. Increment the right pointer until the distance between the right and left is n. Then, increment both pointers until the right pointer reaches the end.

```python
# initialize dummy pointer
# initialize left and right pointers to dummy and head
# (this ensures that the left pointer is one before the node to be      removed, and handles the edge case where there is one node in the list, since it ensures the existence of .next)

# increment right n times

# increment right and left until right is at the end

# set the next of the left pointer to next.next (removes node)

# return next of dummy
```