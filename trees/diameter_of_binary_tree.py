"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0  # height = 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # longest path THROUGH this node
            self.diameter = max(self.diameter, left_height + right_height)

            # return height of this node
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter
    
    

tree = Solution()

root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
left_child_left = TreeNode(4)
left_child_right = TreeNode(5)


root.left = left
root.right = right
left.left = left_child_left
left.right = left_child_right

print(tree.diameterOfBinaryTree(root))