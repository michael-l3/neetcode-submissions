
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #so we are going to build out the graph by seeing if one node can get to the other via dfs a
        #if it cant already get there then we can just build the graph and if it can then we know the one 
        #that we are adding is redundant 
        g = {}

        def dfs(node,target,visted): 
            if node == target: 
                return True 

            #now we process the node 
            visted.add(node) 

            #check its existing nei 
            for nei in g.get(node,[]): 
                if nei not in visted: 
                    if dfs(nei,target,visted): 
                        return True 
            
            return False
    
        for a, b in edges: 
            visted = set()
            #so if we can get to b from a through all of its neighbors, then we know that adding it is the cycle
            if dfs(a,b,visted): 
                return [a,b]
            
            #now if you can get there, then we will establish this connection 
            if a not in g: 
                g[a] = []
            if b not in g: 
                g[b] = []
            g[a].append(b)
            g[b].append(a)            

