"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #we have to create copies of the nodes first 
        #the create a reference to the nodes 
        #grab OG node references to reference new nodes 
        #return the copy 

        if not node: 
            return None

        old_to_new = {} #--> holds the references 

        #create a recursion function that creates node and links it 
        def dfs(curr_node): 
            #base case is if it is already in the old_to_new then we just return the copy node
            if curr_node in old_to_new: 
                return old_to_new[curr_node] 
                
            #if it isnt created already we will create the node 
            copy = Node(curr_node.val)

            #then we put the copy in old_to_new 
            old_to_new[curr_node] = copy

            #now we make the references for the nodes vals 
            for nei in curr_node.neighbors: 
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)