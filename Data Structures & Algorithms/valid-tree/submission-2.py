class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #in order for a tree to valid all nodes must be connected 
        #no cycles in it either 
        #in undirected it can be connected either way 
        #to keep track we will have a parent(node) that shows where the dfs comes from 

        if len(edges) != n -1: 
            return False

        g = {}

        for a,b in edges: 
            if a not in g: 
                g[a] = []
            g[a].append(b)

            if b not in g: 
                g[b] = []
            g[b].append(a)
        
        #we need to keep track of where we are so we will put the first iteration in a set 
        visted = set()

        def dfs(node,parent): 
            if node in visted: 
                return False #- cycle 
            
            visted.add(node)

            for nei in g.get(node,[]): 
                if nei == parent: 
                    continue 
                if not dfs(nei,node): 
                    return False 
            return True 
        
        if not dfs(0,-1): 
            return False 
        
        return len(visted) == n
            
