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

        visited = set()
        def dfs(node): 
            visited.add(node)

            for nei in g.get(node,[]): 
                 if nei not in visited: 
                    dfs(nei)
        
        num_comp = 0 
        for i in range(n): 
            if i not in visited: 
                num_comp += 1 
                dfs(i)
        
        return num_comp
