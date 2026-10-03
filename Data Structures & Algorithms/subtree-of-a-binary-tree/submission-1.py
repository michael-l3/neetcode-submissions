# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        def isSameTree(p,q) -> bool:
            #check first 
            if not p and not q: 
                return True
            if (p and not q) or (q and not p): 
                return False 
            if p.val != q.val: 
                return False
            
            return isSameTree(p.right,q.right) and isSameTree(p.left,q.left) 
        
        if isSameTree(root,subRoot): 
            return True
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        
