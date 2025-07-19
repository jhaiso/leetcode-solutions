# 1233. Remove Sub-Folders from the Filesystem
## Relevant Topics
Sorting

## Solution Thought Process
We notice that the lexicographically smallest elements are the root folders, while the largest are sub-folders. Therefore, we can sort the list of folders, and then iterate through the sorted array.

Time Complexity: O(nlogn)
Space Complexity: O(n)