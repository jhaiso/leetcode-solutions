# 2106. Maximum Fruits Harvested After at Most K Steps
## Relevant Topics
Sliding Window

## Solution Thought Process
For each interval of fruits in the array, we ensure that the number of steps required to visit all fruits within this interval is less than or equal to k.

There are three cases to consider:
1) startPos > fruits[right][0]
Because the interval lies entirely to the left of startPos, we move only to the left to reach fruits[left][0]. Therefore, we need startPos - fruits[left][0] steps.

2) startPos < fruits[left][0]
Because the interval lies entirely to the right of startPos, we move only to the right to reach fruits[right][0]. Therefore, we need fruits[right][0] - startPos steps.

3) startPos within the interval.
We either go left first or go right first, and then travel the length of the interval to get to the other side. Therefore, we need min(fruits[right][0] - startPos, startPos - fruits[left][0]) + fruits[right][0] - fruits[left][0] steps.

Time Complexity: O(n)
Space Complexity: O(1)