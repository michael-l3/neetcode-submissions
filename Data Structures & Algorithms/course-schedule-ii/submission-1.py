class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create a graph that keeps course and prereq 
        #check if there is a cycle and if there is one then we cant take it 
        g = {}
        res = []
        for course,preq in prerequisites: 
            if course in g: 
                g[course].append(preq)
            else:
                g[course] = [preq]
        
        #now we have something like [0:[1],1:[2,3]]
        UNVISITED = 0 
        VISITING = 1 
        VISITED = 2 
        course = [UNVISITED] * (numCourses)

        def dfs(node): 
            state = course[node]

            #check if we are in visiting 
            if state == VISITING:  
                return False 
            elif state == VISITED: 
                return True  
            
            #if neither then we have to change the state 
            course[node] = VISITING 

            #now we have to check it's preReqs 
            for preq in g.get(node,[]): 
                if not dfs(preq): 
                    return False 
            
            #if we got thru then we change to visted and return True 
            course[node] = VISITED
            res.append(node)
            return True
        
        for i in range(numCourses): 
            if not dfs(i): 
                return [] 
        
        return res
