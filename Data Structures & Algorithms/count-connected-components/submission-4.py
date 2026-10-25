class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {} 

        for a,b in edges: 
            if a not in g:
                g[a] = []
            g[a].append(b)

            if b not in g: 
                g[b] = [] 
            g[b].append(a)

        #so we will have a visted set and build out the graph, so everything that is not in visted is a different component 
        def dfs(i): 
            visited.add(i)

            #now we check for the nei to see how many are apart of this component 
            for nei in g.get(i,[]): 
                if nei != i and nei not in visited:
                    dfs(nei)
        
        visited = set() 
        num_components = 0
        for i in range(n): 
            if i not in visited: 
                num_components += 1 
                dfs(i)
            
        return num_components