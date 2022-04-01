from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        positiveDummy = TreeNode(float('inf'))
        negativeDummy = TreeNode(-float('inf'))
        
        def dfs(node, left, right):
            if node:
                # binary search tree가 올바른 경우
                if left.val < node.val and node.val < right.val:
                    # 노들를 왼쪽으로 옮기고 왼쪽 어딘가에 있던 노드는 왼쪽, 원래 노드가 오른쪽
                    # 노드를 오른쪽을 옮기고 원래 노드가 왼쪽, 오른쪽 어딘가에 있던 노드가 오른쪽
                    return dfs(node.left, left, node) or dfs(node.right, node, right)
                # 그렇지 않는 경우
                # swap해 줘야 함
                else:
                    if (left.val < node.val) == False:
                        tempVal = left.val
                        left.val = node.val
                        node.val = tempVal
                        return True
                    else:
                        tempVal = right.val
                        right.val = node.val
                        node.val = tempVal
                        return True
            return False
        # true를 반환하면 swap일 일어나지 않을 때 까지 다시 한다.
        while(dfs(root, negativeDummy, positiveDummy)): #if it returns True, it will run again until no "swaps" are done.
            continue