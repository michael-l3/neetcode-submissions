# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return [] 
        
        res = []
        q = deque() 
        q.append(root)

        while q: 
            a = []
            for _ in range(len(q)): 
                node = q.popleft() 
                a.append(node.val)

                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right) 
            
            res.append(a[-1])
        
        return res



        
