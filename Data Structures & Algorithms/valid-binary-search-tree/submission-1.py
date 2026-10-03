# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #we have to create a fuction that commpares the values 
        #to make sure it is valid 

        def isValid(minn,maxx,node): 
            if not node: 
                return True
            if node.val <= minn: 
                return False 
            if node.val >= maxx: 
                return False
            
            return isValid(minn,node.val,node.left) and isValid(node.val,maxx,node.right)
        
        return isValid(float('-inf'),float('inf'),root)