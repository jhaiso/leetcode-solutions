# 981. Time Based Key-Value Store
## Relevant Topics
Array, Hash Map, Binary Search

## Solution Thought Process
Because the timestamps are strictly increasing, the timestamps of the (value, timestamp) pairs is also strictly increasing. Therefore, we can utilize binary search.