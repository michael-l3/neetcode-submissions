class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {}

        for course,preq in prerequisites: 
            if course in g:
                g[course].append(preq)
            else: 
                g[course] = [preq]
        
        #we need to keep track of current states of where we are at 
        UNVISITED = 0 
        VISITING = 1 
        VISITED = 2 

        states = [UNVISITED] * numCourses 

        def dfs(node): 
            state =  states[node]

            if state == VISITING: 
                return False            #we have a loop 
            if state == VISITED: 
                return True 

            #otherwise that means we are visiting rn 
            states[node] = VISITING 

            #now we must check the preq req of this course that we are taking 
            for preq in g.get(node,[]): 
                if not dfs(preq): 
                    return False 
            
            #if we can get through that then we are done visiting 
            states[node] = VISITED 
            return True
        
        for i in range(numCourses): 
            if not dfs(i): 
                return False 
        
        return True 