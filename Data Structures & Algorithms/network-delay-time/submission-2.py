import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #djk algo for min time 
        g = {}
        
        for ui,vi,ti in times: 
            if ui not in g: 
                g[ui] = []
            g[ui].append((ti,vi))
        
        #we want a min heap
        #and something to keep track of the smallest already bc if we have seen it it means it is the smallest from popping 
        heap = [(0,k)]   #--> cost 0 to start
        #time can only go to its neighbors 
        visited = set()
        minTime = {}

        while heap:
            cost,node = heapq.heappop(heap)
            if node in visited: 
                continue 

            visited.add(node) #we do this to know that this has the min time alr, dont need to revisit
            minTime[node] = cost

            #now we check the nei
            for distance,new_node in g.get(node,[]):
                heapq.heappush(heap,(distance+cost,new_node))
        
        if len(visited) != n: 
            return -1

        return max(minTime.values())
