# 3343. Maximum Manhattan Distance After K Changes
## Relevant Topics
String, Hash Table, Greedy

## Solution Thought Prcoess
Looking at the definition of Manhattan Distance (and assuming it's named so because you cant go through bulidings and can only go on streets and avenues in Manhattan), we can see that distance is linearly related to both axes. Additionally, if we find the maximal direction, changing the opposite direction to that direction increases distance by 2.

My immediate thoughts are to count the occurences of each character, and use a greedy algorithm to change the smaller opposing direction to the opposite. (This maximizes the change in distance from each change: +2). 