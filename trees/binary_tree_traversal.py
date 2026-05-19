class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class Tree:
    """
    Most tree recursion follows:
    answer(node) =
        combine(
            answer(node.left),
            answer(node.right)
        )
    """
    def __init__(self):
        pass
    
    def preOrder(self, root):
        """
        This gets the parent first, then goes on to explore the children.
        preorder is a top down approach
        """
        
        if not root:
            return
        
        print(root.value)
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    def inOrder(self, root):
        """
        This goes from left_child -> Root -> right_child
        I slot myself between my children
        """
        
        if not root:
            return
        
        self.inOrder(root.left)
        print(root.value)
        self.inOrder(root.right)
        
    def postOrder(self, root):
        """
        This uses a bottom to top approach, it gets the children first and then their parents
        """
        if not root:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.value)
        
    def countLeafNodes(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        return self.countLeafNodes(root.left) + self.countLeafNodes(root.right)
        
    def countNodes(self, root):
        if not root:
            return 0
        
        total = 1 + (self.countNodes(root.left) + self.countNodes(root.right))
        return total
    
    def max_depth(self, root):
        
        if not root:
            return 0
        
        max_ = 1 + max(self.max_depth(root.left), self.max_depth(root.right))
        return max_
    
    def search(self, root, target):
        if not root:
            return False
        
        if root.value == target:
            return True
        
        left = self.search(root.left, target)
        right = self.search(root.right, target)
        
        
        return left or right
    
    def sumLeft(self, root):
        
        def dfs(root, isLeft):
            if not root:
                return 0
            
            if not root.left and not root.right and isLeft:
                return root.value
            
            left = dfs(root.left, True) 
            right = dfs(root.right, False)
            
            return left + right
        
        return dfs(root, False)
            
        
        
tree = Tree()

root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
left_child_left = TreeNode(4)
left_child_right = TreeNode(5)


root.left = left
root.right = right
right.left = left_child_left
right.right = left_child_right

# tree.preOrder(root=root)
# print("\n")
# tree.inOrder(root=root)
# print("\n")
# tree.postOrder(root=root)

# print(tree.max_depth(root=root))
# print(tree.countLeafNodes(root=root))
# print(tree.search(root=root, target='G'))
print(tree.sumLeft(root=root))