class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_elements_within_range(node, range):
    low = range[0]
    high = range[1]
    sum = 0
    if node is None:
        return 0
    if node.value > high:
        return sum_of_elements_within_range(node.left, range)
    if node.value < low:
        return sum_of_elements_within_range(node.right, range)
    if node.value >= low and node.value <= high:
        sum += node.value
        sum += sum_of_elements_within_range(node.left, range)
        sum += sum_of_elements_within_range(node.right, range)
    return sum  

tree = BinaryTree(5)
tree.left = BinaryTree(3)
tree.right = BinaryTree(8)
tree.left.left = BinaryTree(2)
tree.left.right = BinaryTree(4)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(10)

print(sum_of_elements_within_range(tree, [4, 9]))  # Output: 23

tree = BinaryTree(5)
tree.left = BinaryTree(3)
tree.right = BinaryTree(8)
tree.left.left = BinaryTree(2)
tree.left.right = BinaryTree(4)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(10)

print(sum_of_elements_within_range(tree, [6, 10]))  # Output: 24

tree = BinaryTree(5)
tree.left = BinaryTree(3)
tree.right = BinaryTree(8)
tree.left.left = BinaryTree(2)
tree.left.right = BinaryTree(4)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(10)

print(sum_of_elements_within_range(tree, [1, 4]))  # Output: 9

tree = BinaryTree(1)

print(sum_of_elements_within_range(tree, [1, 1]))  # Output: 1

# function optimized

def sum_of_elements_within_range_improved(node, low, high):
    
    if node is None:
        return 0
    
    if node.value < low:
        return sum_of_elements_within_range_improved(node.right, low, high)
    
    if node.value > high:
        return sum_of_elements_within_range_improved(node.left, low, high)
    
    return (node.value + sum_of_elements_within_range_improved(node.left, low, high) + sum_of_elements_within_range_improved(node.right, low, high))

print("Improved function")

# Example usage
tree = BinaryTree(5)
tree.left = BinaryTree(3)
tree.right = BinaryTree(8)
tree.left.left = BinaryTree(2)
tree.left.right = BinaryTree(4)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(10)

print(sum_of_elements_within_range_improved(tree, 4, 9))  # Output: 23