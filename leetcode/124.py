class Solution:
    # 기본적으로 순회하면서 왼, 오 부트리의 MPS(부모 포함, 포함x)를 기억한다.
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node.left and not node.right:
                return node.val, float('-inf')
            left_i = left_e = right_i = right_e = float('-inf')
            
            if node.left:
                left_i, left_e = dfs(node.left)
            if node.right:
                right_i, right_e = dfs(node.right)
            
            
            #node.val+left_i+right_i이것은 왜 sum_e(node를 부모 제외) 인 케이스인가?
            sum_i = max(left_i+node.val, right_i+node.val, node.val)
            sum_e = max(left_i, left_e, right_i, right_e, node.val+left_i+right_i)
            return (sum_i, sum_e)
        
        return max(dfs(root))