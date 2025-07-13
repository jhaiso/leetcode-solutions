# 2410. Maximum Matching of Players With Trainers

## Relevant Topics

Greedy

## Solution Thought Process

Since the trainers and players can only have individual matches, and a trainer MUST have a training capacity greater than or equal to the player, we can take a greedy approach. At each step, we take the trainer with the largest capacity and check if they are compatible with the palyer of the largest capacity. If they are, then that is a match! If not, that player doesn't get a trainer (poor player lol)

```python
# sort players and trainers in descending order
# initialize two pointers
# initialize count
# while neither pointer is past the end of their respective arrays
#   if criteria is met
#       increment trainer
#       increase count
#   increment player
```
Time Complexity: O(mlogm + nlogn) - sorting
Space Complexity: O(logm + logn)