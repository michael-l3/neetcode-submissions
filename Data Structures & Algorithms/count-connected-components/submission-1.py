class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #we are going to have to have a components variables to keep track of connected things 
        #i believe a set as well 

        g = {} 

        for a,b in edges: 
            if a not in g: 
                g[a] = []
            if b not in g: 
                g[b] = []
            g[a].append(b)
            g[b].append(a)

        #now we have the nodes connected to each other and relationships 
        visited = set()

        def dfs(node): 
            visited.add(node)
            for nei in g.get(node,[]):
                if nei not in visited: 
                    dfs(nei) 
        
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)

        return components