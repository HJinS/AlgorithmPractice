from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        Q = deque()
        Q.append([root, 1])
        res = 0
        while Q:
            node, level = Q.popleft()
            res = max(res, level)
            if node.left != None:
                Q.append([node.left, level+1])
                
            if node.right != None:
                Q.append([node.right, level+1])
                
                
        return res