# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(minn,maxx,node): 
            if not node: 
                return True 
            if node.val <= minn or node.val >= maxx: 
                return False 

            return dfs(minn,node.val,node.left) and dfs(node.val,maxx,node.right) 
        
        return dfs(float("-inf"),float("inf"),root)