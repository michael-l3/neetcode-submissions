class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {}
        #we need to construct the graphs of what we need to take in order to take waht 
        for i in range(numCourses): 
            g[i] = [] 
        
        for course,preq in prerequisites: 
            g[course].append(preq)
        
        #so now we have all the classes we want to take and all of its preq
        #we need to traverse thru the graph to see if we can take all of the classes 
        UNVISTED = 0 
        VISITING = 1 
        VISITED = 2 
        states = [UNVISTED] * (numCourses)

        def dfs(node): 
            state = states[node]

            #if we VISTING that measn loop 
            if state == VISITING: 
                return False 
            if state == VISITED: 
                return True 
            
            #if neither that means that this is first time seeing 
            states[node] = VISITING 

            #now we need to see if we need to take any other classes in order to take this one 
            for preq in g[node]: 
                if not dfs(preq): 
                    return False 
            
            #and if we can then we will change to visted bc we can take the class 
            states[node] = VISITED 
            return True

        for i in range(numCourses): 
            if not dfs(i): 
                return False

        return True 
