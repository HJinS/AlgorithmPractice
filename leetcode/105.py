# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_idx
            
            if left > right:
                return None
            
            root_val = preorder[preorder_idx]
            root = TreeNode(val=root_val)
            preorder_idx += 1
            
            root.left = array_to_tree(left, inorder_map[root_val]-1)
            root.right = array_to_tree(inorder_map[root_val]+1, right)
            
            return root
        
        preorder_idx = 0
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
            
        return array_to_tree(0, len(preorder)-1)