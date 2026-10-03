# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #everything on left of root is smaller so we have to go down there first 
        #decrement k 

        counter = 0
        answer = None

        def dfs(node): 
            nonlocal counter,answer

            if not node:
                return None

            #check left first 
            dfs(node.left)  
            counter += 1 

            if counter == k: 
                answer = node.val
                return
            
            #checkright after 
            dfs(node.right)
        
        dfs(root)
        return answer
            
