# 287. Find the Duplicate Number

## Relevant Topics

Array, Linked List, Hash Set, Floyd's Algorithm

## Solution Thought Process

### Hash Set

Because we're checking for duplicates, we could iterate through the list and add the values to a hash set. We can check if the current value is already in the set in O(1) time.
Time Complexity: O(n)
Space Complexity: O(n)

### Floyd's Algorithm

Because the array contains n+1 integers with each integer in the range [1,n], we can treat the array as a linked list. Each value acts as a pointer to the index of the next number. Since no element points to null, and at least two pointers will point to the same index, there must exist a cycle such that the start of the cycle is the repeated number (since multiple nodes point to that value). We can apply Floyd's Algorithm!

```python
# utilize a fast and slow pointer to find the cycle

# create a new slow pointer at the start
# increment both equally until the start is found
# (this works because the distance between where the fast and slow pointer intersect and the beginning of the cycle is equal to that of the distance between the beginning of the linked list and the beginning of the cycle)
```