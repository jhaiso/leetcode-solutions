# 3445. Maximum Difference Between Even and Odd Frequency II
## Relevant Topics
Sliding Window, Monotonic Queue

## Solution Thought Process
### Brute Force
For every substring in the string, calculate the frequencies. Then, find the largest odd frequency, and smallest even frequency, and update the maximum difference.
Time Complexity: O(n^2 * k^2)
Space Complexity: O(n)

### Sliding Window
Since the string only contains digit characters [0,4], we can enumerate the characters a and b. There are 4 possible cases [00, 01, 10, 11] where the parity of each character is represented by a binary bit.

We iteratively increase the right pointer, and update the count of a and b up to the right index. The state can be represented as an integer:
status = (count(a) % 2) * 2 + (count(b) % 2).

Then, we increment the left pointer such that the indeces <= left can serve as the left side of a valid substring. We record the previous counts of the values. We increment left only when (1) the substring length is at least k, (2) count(b) - previous(b) >= 2 (b appreas an even number of times, but zero occurences must be excluded).

For any valid left, the result is difference of counts without their prefix sums: (count(a) - count(b)) - (prev(a) - prev(b)). We can maintain an array to keep track of the minimum value of prev(a) - prev(b).

status = (prev(a) % 2) * 2 + (prev(b) % 2)

We are looking for substrings with state (10) base-2, so teh left endpoint mus thave the state status_right XOR (10) base-2.