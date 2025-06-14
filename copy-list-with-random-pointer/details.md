# 138. Copy List with Random Pointer

## Related Topics

Linked List, Hash Map

## Solution Thought Process

### Hash Map

Since we are making a deep copy, the random pointers could point to a node that doesn't exist yet. (Unlike making a deep copy of a normal linked list, where the node is guaranteed to point to the next node, so a new node can be created to accomodate it and still be accessed). Therefore, we should use a hashmap to map the old nodes to the new nodes.

```python
# initialize map and set values
# set key None to value None (accomodates empty list, last node, and nodes that randomly point to None)

# while the current node exists
#   set the value of the new node to that of the old node
#   set next of the new node to the corresponding new node
#   set the random of the new node to the corresponding new node

# return the new head
```

Time Complexity: O(n)
Space Complexity: O(n)

### Space Optimization

To reduce the space complexity from the allocation of the hash map, we could imbed the copy inside the current list (i.e. we set the next pointer of each old node to the corresponding new node, and the next pointer of those nodes to the next old node.). Then, the random pointers can be set to the next of the old randoms. Lastly, the next pointers can be moved to the appropriate node versions.

Time Complexity: O(n)
Space Complexity: O(1)