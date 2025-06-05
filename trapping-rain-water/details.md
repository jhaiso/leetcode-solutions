# 42. Trapping Rain Water
## Relevant Topics
Array, Stack, Two Pointers

## Solution Thought Process
### Brute Force
At each elevation, we expand to the left and right to find the local maximum in each side. Then we take the smaller of the two and fill the elevation to the smaller maxima - current elevation.
Time Complexity: O(n^2)
Space Complexity: O(1)

### Two Pointers
We see that wee are looking for the smaller of two local maximums on either side. Therefore, if we know that a local maxima on one side is smaller than the local maxima on the other side, we know that we can fill the elevation on the side with the smaller local maxima.