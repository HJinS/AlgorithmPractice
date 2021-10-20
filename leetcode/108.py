# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def to_binaryTree(nums):
            if not nums:
                return None
            length = len(nums)
            node = TreeNode(nums[length//2])
            node.left = to_binaryTree(nums[:length//2])
            node.right = to_binaryTree(nums[length//2+1:])
            return node
        
        return to_binaryTree(nums.copy())