class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {}

        for course,preq in prerequisites: 
            if course in g:
                g[course].append(preq)
            else: 
                g[course] = [preq]
        
        UNVISITED = 0 
        VISITING = 1 
        VISITED = 2 

        states = [UNVISITED] * numCourses 
        res = []
        def dfs(i): 
            state = states[i]

            if state == VISITING: 
                return False 
            if state == VISITED: 
                return True 
            
            states[i] = VISITING 

            for preq in g.get(i,[]): 
                if not dfs(preq): 
                    return False 
            
            #otherwise we made it through 
            states[i] = VISITED 
            res.append(i)
            return True 

    
        for i in range(numCourses): 
            if not dfs(i): 
                return []

        return res
        