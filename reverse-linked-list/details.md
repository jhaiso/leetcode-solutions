# 206. Reverse Linked List
## Relevant Topics
Linked List, Recursion

## Solution Thought Process
### Iteration
We iterate through the nodes, and at each node, we set the next pointer to the previous node. (We must keep a temporary node to increment the current node after reversing the next pointer)
Time Complexity: O(n)
Space Complexity: O(1)

### Recursion
We recursively call the function on a linked list starting from the next node of the current node. After the recursive call, we reverse the first node in the sublist.
Time Complexity: O(n)
Space Complexity: O(n)