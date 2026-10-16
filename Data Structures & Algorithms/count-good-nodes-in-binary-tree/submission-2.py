# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0 

        def dfs(node,maxVal): 
            nonlocal goodNodes 

            if not node: 
                return
            
            if node.val >= maxVal: 
                goodNodes += 1 

            maxVal = max(maxVal, node.val)
            dfs(node.left,maxVal)
            dfs(node.right,maxVal)

        dfs(root,root.val)
        return goodNodes