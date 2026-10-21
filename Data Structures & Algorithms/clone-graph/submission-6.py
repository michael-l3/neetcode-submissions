"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #so the way we are going to sovle this is by creating a old_to_new hashmap 
        #create all of the nodes first 
        #then connect them with each other 
        if not node: 
            return None
        o_t_n = {} 

        #write this in one function so that we are able to call the variables  
        def dfs(node): 
            if node in o_t_n: 
                return o_t_n[node]  #-> returning the copy 

            #otherwise we must create the copy node 
            new_node = Node(node.val)
            o_t_n[node] = new_node 

            #now we must find the nei for that node 
            for nei in node.neighbors: 
                new_node.neighbors.append(dfs(nei))

            return new_node 
        
        return dfs(node)
    

        