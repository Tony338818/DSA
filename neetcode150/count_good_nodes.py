"""
Given a binary tree root, a node X in the tree is named good if in the path from 
root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
def countGoodNodes(root: TreeNode):
    
    def dfs(node, current_max):
        if not node:
            return 0
        
        count = 0
        
        if node.value >= current_max:
            count = 1
            
        current_max = max(current_max, node.value)
        
        count += dfs(node.left, current_max)
        count += dfs(node.right, current_max)
        
        return count
    
    return dfs(root, root.value)
    

root = TreeNode(3)
cold = TreeNode(1)
hot = TreeNode(4)
cola = TreeNode(3)
coffee = TreeNode(1)
tea = TreeNode(5)
sprite = TreeNode(1)

root.left = cold
root.right = hot

cold.left = cola
# cold.right = sprite

hot.left = coffee
hot.right = tea

result = countGoodNodes(root=root)
print(result)
