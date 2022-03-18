# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def construct(self, low, high):
        if low == high:
            return [TreeNode(low)]
        # low가 더 크면 트리를 만들 수 없음
        if low > high:
            return [None]
        res = []
        
        # 1 ~ n 까지 노드를 가지고 트리를 구축 함
        # 재귀적으로 1~mid-1, mid+1~n 까지 트리 구축
        # 그 결과를 가지고 현재 노드 mid 의 트리를 구축 하고 반환
        # 1~n의 값이 root일 경우에 각각 자식을 재귀의 형태로 구함
        for i in range(low, high+1):
            left = self.construct(low, i-1)
            right = self.construct(i+1, high)
            # 각각의 left와 right의 노드들을 현재 노드 mid의 left, right로 구축후 res에 추가
            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res
    
    def generateTrees(self, n: int):
        return self.construct(1, n)