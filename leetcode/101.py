class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)