# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0 

        if not root: 
            return 0 
        
        #create some dfs function that compares the node that we are at with the previous node and if it > we are good 
        def dfs(node,maxVal): 
            nonlocal goodNodes

            if not node: 
                return

            val = node.val 
            #question but what if there is something in between that is greater than the previous node val, how 
            #do we keep history of that, thru maxVal of the max
            if val >= maxVal: 
                goodNodes += 1 

            maxVal = max(maxVal,val)
            dfs(node.left,maxVal)
            dfs(node.right,maxVal)
        
        #start at 0 because this is the root and it can be anythin
        dfs(root,root.val)
        return goodNodes