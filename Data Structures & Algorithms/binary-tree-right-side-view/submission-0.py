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
        #this will use bfs 
        q = deque() 
        res = []
        q.append(root)
        
        while q: 
            qLength = len(q)

            for i in range(1,qLength+1): 
                node = q.popleft()
                val = node.val 

                if i == qLength: 
                    res.append(val)
            
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
        
        return res


