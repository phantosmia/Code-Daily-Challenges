class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def construct_bst_from_postorder(postorder): # [2, 4, 3, 8, 7, 5]
    if not postorder:
        return None
    
    def construct(start, end): # 0, 5
        if start > end:
            return None
        root_val = postorder[end] # 5
        root = TreeNode(root_val) # 5
        index = start # 0
        while index <= end - 1 and postorder[index] < root_val: # 0 <= 2 and 2 < 8
            index += 1 # 3
        root.left = construct(start, index - 1) # 0, 2
        root.right = construct(index, end - 1)  # 2, 2
        return root 
    return construct(0, len(postorder) - 1)

def print_tree(node, level=0, prefix="Root: "):
    if not node:
        return
    print(" " * (level * 4) + prefix + str(node.val))
    if node.left:
        print_tree(node.left, level + 1, "L--- ")
    if node.right:
        print_tree(node.right, level + 1, "R--- ")

postorder = [2, 4, 3, 8, 7, 5]
root = construct_bst_from_postorder(postorder)
print_tree(root)