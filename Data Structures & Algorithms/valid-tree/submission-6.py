class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #undirected meaning no dependencies 
        #tree theory is that if we have n nodes that a valid would have n - 1 edges 
        #we will keep what we have visted in set 

        g = {} 

        for a,b in edges: 
            if a not in g:
                g[a] = []
            g[a].append(b)

            if b not in g: 
                g[b] = [] 
            g[b].append(a)

        def dfs(i,parentNode): 
            if i in visited: 
                return False 

            visited.add(i)

            #now we look through it's neighbors 
            for nei in g.get(i,[]): 
                if nei not in visited and nei != parentNode: 
                    if not dfs(nei,i): 
                        return False 
            
            return True
        

        #so for this one it would work if we keep track of a set and it's parent node 
        visited = set() 
        dfs(0,-1)
        return len(visited) == len(edges) + 1


