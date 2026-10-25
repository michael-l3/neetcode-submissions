class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def dfs(i,target,visited): 
            #we can get to target another way already
            if i == target: 
                return True 
            
            visited.add(i)

            #check if the nei can get to the target 
            for nei in g.get(i,[]): 
                if nei != i and nei not in visited: 
                    if dfs(nei,target,visited): 
                        return True 
            
            return False
            
        g = {} 
        #we need to keep track of nodes that we have already visited and if we can get to the target node 
        #another way 
        for a,b in edges: 
            visited = set() 
            
            if dfs(a,b,visited):  #this means we can get to the target already through another path
                return [a,b]
        
            if a not in g: 
                g[a] = []
            if b not in g: 
                g[b] = []
            g[a].append(b)
            g[b].append(a)    
            

        