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
        leafs = 0
        
        def count(root, leafs):
            if not root:
                leafs += 1
                return
            
            count(root.left)
            count(root.right)
            
        count(root, leafs=leafs)  
        print(leafs)
        
        
tree = Tree()

root = TreeNode('A')
left = TreeNode('B')
right = TreeNode('C')
left_child_left = TreeNode('D')
left_child_right = TreeNode('E')


root.left = left
root.right = right
left.left = left_child_left
left.right = left_child_right

# tree.preOrder(root=root)
# print("\n")
# tree.inOrder(root=root)
# print("\n")
# tree.postOrder(root=root)

tree.countLeafNodes(root=root)