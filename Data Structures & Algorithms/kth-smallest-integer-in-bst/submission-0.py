# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #dfs down the left side first
        counter = 0 
        answer = None

        def dfs(node): 
            nonlocal counter, answer 

            if not node: 
                return 
            
            dfs(node.left)

            counter += 1 
            if counter == k: 
                answer = node.val 
                return 
            
            dfs(node.right)
        
        dfs(root)
        
        return answer