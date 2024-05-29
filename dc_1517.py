class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_unival_subtrees(node):
    def helper(node):
        if node is None:
            return 0, True
        
        left_count, is_left_unival = helper(node.left)
        right_count, is_right_unival = helper(node.right)
        
        total_count = left_count + right_count
        
        if is_left_unival and is_right_unival:
            if node.left and node.data != node.left.data:
                return total_count, False
            if node.right and node.data != node.right.data:
                return total_count, False
            return total_count + 1, True
        
        return total_count, False

    count, _ = helper(node)
    return count

tree = Tree(0)
tree.left = Tree(1)
tree.right = Tree(0)
tree.right.left = Tree(1)
tree.right.right = Tree(0)
tree.right.left.left = Tree(1)
tree.right.left.right = Tree(1)
print(count_unival_subtrees(tree))  # Output: 5
