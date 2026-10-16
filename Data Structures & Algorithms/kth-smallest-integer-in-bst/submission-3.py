# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        kSmallest = None  
        #once this counter hits k, then we return number 

        def dfs(node): 
            nonlocal counter 
            nonlocal kSmallest

            if not node: 
                return 
            
            dfs(node.left)
            counter += 1 

            if counter == k:
                kSmallest = node.val 
                return 
            
            #after that we check the right side 
            dfs(node.right)
        
        dfs(root)
        return kSmallest