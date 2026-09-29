class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #so we will make an adjacent list with the course and preReq 
        g = {}
        for i in range(numCourses):
            g[i] = []

        for course, preReq in prerequisites: 
                g[course].append(preReq)

        #states 
        UNVISTED = 0 
        VISTING = 1 
        VISTED = 2 

        states = [UNVISTED] * numCourses 

        def dfs(node): 
            state = states[node]

            if state == VISTED: 
                return True 
            if state == VISTING: 
                return False 
            
            states[node] = VISTING 

            for nei in g[node]: 
                if not dfs(nei): 
                    return False 

            states[node] = VISTED 
            return True 

        for i in range(numCourses): 
            if not dfs(i): 
                return False 
        
        return True