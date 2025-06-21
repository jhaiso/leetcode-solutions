# 230. Kth Smallest Element in a BST

## Relevant Topics

Tree, Binary Search Tree, Inorder Traversal

## Solution Thought Process
In a binary search tree, the smallest value is found by traversing to the left child until the last one. In looking at the example problems and visualizing, we see that from the smallest node, we traverse upwards, and explore the right subtree in the same order when available. Because we are going 'up' the tree, and going left to right, an inorder traversal would be appropriate.