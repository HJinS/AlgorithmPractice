class Solution:
    res = False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.check(root)
        return self.res
        
        
    def check(self, node):
        if node.left == None and node.right == None:
            return node.val, node.val
        
        elif node.left == None and node.right != None:
            r_max, r_min = self.check(node.right)
            if node.val >= r_min:
                self.res = False
            return max(r_max, node.val), min(r_min, node.val)
        elif node.left != None and node.right == None:
            l_max, l_min = self.check(node.left)
            if node.val <= l_max:
                self.res = False
            return max(l_max, node.val), min(l_min, node.val)
        
        else:
            l_max, l_min = self.check(node.left)
            r_max, r_min = self.check(node.right)
            
            if not (l_max < node.val < r_min):
                self.res = False
            return max(r_max, node.val), min(l_min, node.val)
            
        