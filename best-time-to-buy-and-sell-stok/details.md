# 121. Best Time To Buy And Sell Stock

## Relevant Toptics

Array, Sliding Window, Dynamic Programming

## Solution Thought Process

### Brute Force

Calculate every possible combination of buy and sells and return the largest.
Time Complexity: O(n^2)

### Two Pointers

By definition, we have to buy a stock before we sell. To maximize our profit, we must buy at the lowest prices before our decided sell price. So, we can keep two pointers. At each step we increment the sell pointer and calculate the profit. If it is negative (a new lowest prices if found), we update the buy pointer to the new minimum.
Time Complexity: O(n)
Space Complexity: O(1)

### Dynamic Programming / Iteration

At each step, if we know the minimum up until that price, we can find the maximum profit at that position in the timeline. Therefore, we can use a variable to keep track of the current minimum, and simply iterate through the prices. Therefore, this approach is faster, since we only iterate through the array 1 time. It is also more space efficient, since one less variable is allocated (two pointers --> minimum)
Time Complexity: O(n)
Space Complexity: O(1)
