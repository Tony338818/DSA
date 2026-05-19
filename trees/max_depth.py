"""
Given the root of a tree:
find the maximum depth
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def max_depth(self, root):
        if not root:
            return 0
        
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))