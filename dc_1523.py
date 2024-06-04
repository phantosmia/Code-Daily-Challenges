class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def find_largest(node):
    current = node
    while current.right:
        current = current.right
    return current

def find_second_largest(root):
    if root is None or (root.left is None and root.right is None):
        return None
    
    current = root
    while current:
        if current.left and not current.right:
            return find_largest(current.left).root
        if current.right and not current.right.left and not current.right.right:
            return current.root
        current = current.right



root = Tree(10)
root.left = Tree(5)
root.right = Tree(15)
root.right.right = Tree(20)
root.right.right.left = Tree(18)

print(find_second_largest(root))