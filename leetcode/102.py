from collections import deque
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        Q = deque()
        Q.append(root)
        res = []
        if root == None:
            return []
        while Q:
            cnt = len(Q)
            idx = 0
            order = []
            while idx < cnt:
                node = Q.popleft()
                order.append(node.val)
                if node.left != None:
                    Q.append(node.left)
                if node.right != None:
                    Q.append(node.right)
                idx += 1
            res.append(order.copy())
                
        return res