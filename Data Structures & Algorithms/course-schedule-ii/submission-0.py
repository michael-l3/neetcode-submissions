class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #so we will make an adjacent list with the course and preReq 
        res = []
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
            res.append(node)
            return True 

        for i in range(numCourses): 
            if states[i] == UNVISTED:
                if not dfs(i): 
                    return [] 
        
        return res
