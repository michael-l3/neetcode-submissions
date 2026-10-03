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

        o_t_n = {}  #this is how we will reference everythign so the 
        #new nodes know where to go 

        def dfs(curr_node): 
            if curr_node in o_t_n: 
                return o_t_n[curr_node] #-> this will return the copy
            
            #now lets say it isnt, that means we havent made the copy yet 
            copy = Node(curr_node.val)

            o_t_n[curr_node] = copy 

            #after we made the copy of the node we have to do their neighbors 
            for nei in curr_node.neighbors: 
                #now we need the copy to have its neighbors 
                copy.neighbors.append(dfs(nei))
            
            return copy
            
        
        return dfs(node)