from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
Q = deque()
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root == None:
            return
        while root != None:
            if root.left != None:
                l = root.left
                while l.right != None:
                    l = l.right
                l.right = root.right
                root.right = root.left
                root.left = None
            root = root.right