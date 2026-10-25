"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #so what we are going to do it create an adjac list 
        #create the nodes while we are at it 
        #keep track of which ones we created via dictionary 
        if not node: 
            return None
        g = {}

        def dfs(node): 
            #if it is in the graph it is already created 
            if node in g: 
                return g[node]

            #otherwise the copy needs to be created 
            newNode = Node(node.val)
            g[node] = newNode 

            #now we just have to connect the neighbors while creating them 
            for nei in node.neighbors: 
                newNode.neighbors.append(dfs(nei))
            
            return g[node] #returning copy node
        dfs(node)
        return g[node]
