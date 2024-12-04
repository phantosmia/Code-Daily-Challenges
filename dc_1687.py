from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDeepestNode(root):
    if not root:
        return None
    q = deque([root])
    deepest_node = None

    while q:
        node = q.popleft()
        deepest_node = node

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return deepest_node.val

root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.left.left = TreeNode("d")
root.left.right = TreeNode("e")

print(findDeepestNode(root))